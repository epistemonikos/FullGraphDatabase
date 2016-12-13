# -*- coding: utf-8 -*-

from logs.log import Log
from model.primary_study_comparator import PrimaryStudyComparator
from fuzzywuzzy import fuzz as fuzzy_distance
from Levenshtein import distance as levenshtein_distance
from model.string_helpers import without_stop_words

LOG_FILE_PATH = "resources/logs/primary_study_comparator_log.log"

@Log(PrimaryStudyComparator, PrimaryStudyComparator.equal_title)
def equal_title_log(self, title, returned):
  file = open(LOG_FILE_PATH, "a")
  self_title = self.primary_study.get_title() or 'None'
  file.write( "{}\t{}\t{}\t{}\n".format('equal_title', self_title, title, returned) )
  file.close()

@Log(PrimaryStudyComparator, PrimaryStudyComparator.equal_doi)
def equal_doi_log(self, doi, returned):
  file = open(LOG_FILE_PATH, "a")
  self_doi = self.primary_study.get_doi() or 'None'
  file.write( "{}\t{}\t{}\t{}\n".format('equal_doi', self_doi, doi, returned) )
  file.close()

@Log(PrimaryStudyComparator, PrimaryStudyComparator.equal_pubmed_id)
def equal_pubmed_id_log(self, pubmed_id, returned):
  file = open(LOG_FILE_PATH, "a")
  self_pubmed_id = self.primary_study.get_pubmed_id() or 'None'
  file.write( "{}\t{}\t{}\t{}\n".format('equal_pubmed_id', self_pubmed_id, pubmed_id, returned) )
  file.close()

@Log(PrimaryStudyComparator, PrimaryStudyComparator.equal_citation)
def equal_citation_log(self, other_citation, returned):
  ratio_1 = 0
  ratio_2 = 0
  ratio = 0
  if returned:
    self_citation = self.primary_study.get_citation()
    c1 = self.__normalize_citation__(other_citation)
    c2 = self.__normalize_citation__(self_citation)
    min_cita = c1
    if len(c1) > len(c2):
      min_cita = c2
    max_cita = c1
    if len(c1) < len(c2):
      max_cita = c2
    len_max_cita = len(max_cita)
    len_min_cita = len(min_cita)
    count = 0 
    for x in min_cita:
      if x in max_cita:
        count += 1
        max_cita.remove(x)
    ratio_1 = count/len_max_cita*100
    ratio_2 = fuzzy_distance.token_set_ratio(self_citation, other_citation)
    ratio = (ratio_1 + ratio_2)/2
  file = open(LOG_FILE_PATH, "a")
  self_citation = self.primary_study.get_citation() or 'None'
  file.write( "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format('equal_citation', self_citation, other_citation, returned, ratio_1, ratio_2, ratio) )
  file.close()
