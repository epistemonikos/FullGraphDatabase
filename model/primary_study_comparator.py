# -*- coding: utf-8 -*-
from fuzzywuzzy import fuzz as fuzzy_distance
from Levenshtein import distance as levenshtein_distance
from model.string_helpers import without_stop_words

class PrimaryStudyComparator:

  MAX_TITLE_DISTANCE = 10
  MIN_RATIO_FOR_CITATIONS = 75

  def __init__(self, primary_study):
    self.primary_study = primary_study

  def equal_to(self, other):
    self_pubmed_id = self.primary_study.get_pubmed_id()
    self_doi = self.primary_study.get_doi()
    self_title = self.primary_study.get_title()
    self_citation = self.primary_study.get_citation()
    return (
        other.equal_pubmed_id(self_pubmed_id) or
        other.equal_doi(self_doi) or
        other.equal_title(self_title) or
        other.equal_citation(self_citation)
      )

  def equal_title(self, other_title):
    self_title = self.primary_study.get_title()
    if self_title and other_title:
      distance = levenshtein_distance(self_title, other_title)
      return distance < self.MAX_TITLE_DISTANCE

  def equal_doi(self, other_doi):
    self_doi = self.primary_study.get_doi()
    if self_doi and other_doi:
      return self_doi == other_doi
    return False

  def equal_pubmed_id(self, other_pubmed_id):
    self_pubmed_id = self.primary_study.get_pubmed_id()
    if other_pubmed_id and self_pubmed_id:
      return self_pubmed_id == other_pubmed_id
    return False

  def equal_citation(self, other_citation):
    self_citation = self.primary_study.get_citation()
    if self_citation and other_citation:

      # normalizar las citas y dejarla como arreglo
      c1 = self.__normalize_citation__(other_citation)
      c2 = self.__normalize_citation__(self_citation)

      #encontrar la cita mas larga (max_cita) y la cita mas corta (min_cita)
      min_cita = c1
      if len(c1) > len(c2):
        min_cita = c2
      max_cita = c1
      if len(c1) < len(c2):
        max_cita = c2
      len_max_cita = len(max_cita)
      len_min_cita = len(min_cita)

      #número de elementos en min_cita que están tambien en max_cita
      count = 0 
      for x in min_cita:
        if x in max_cita:
          count += 1
          max_cita.remove(x)

      #invento de fuzzy match
      ratio_1 = count/len_max_cita*100

      #típico fuzzy set match
      ratio_2 = fuzzy_distance.token_set_ratio(self_citation, other_citation)

      #ratio final para decidir
      ratio = (ratio_1 + ratio_2)/2
      return ratio >= self.MIN_RATIO_FOR_CITATIONS
    return False

  def __normalize_citation__(self, citation):

    #quitar puntuacion
    normalized = citation.replace('.',' ')
    normalized = citation.replace(',',' ')
    normalized = citation.replace(';',' ')

    #quitar stop_words y hacer un arreglo de tokens
    normalized = without_stop_words(normalized.lower()).split()

    #quitar palabras demasiado cortas
    normalized = [x for x in normalized if len(x) > 2]

    return normalized