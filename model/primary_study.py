from model.node import Node
from Levenshtein import distance as levenshtein_distance
import re

class PrimaryStudy(Node):

  MAX_CITATION_DISTANCE = 20
  MAX_TITLE_DISTANCE = 10
  MAX_CITATION_TITLE_DISTANCE = 5
  
  def klass(self):
    return 'PS'

  def exist_in(self, graph):
    def orientdb_to_dict(odb):
        info ={}
        info['authors'] = odb.authors
        info['ids'] = odb.ids
        info['abstract'] = odb.abstract
        info['title'] = odb.title
        info['publication_info'] = odb.publication_info
        info['keywords'] = odb.keywords
        info['citation'] = odb.citation
        info['references'] = odb.references
        info['reference'] = odb.reference
        return info
    results = graph.execute('select * from PS') #an array of orientDB Object
    for orientdb_object in results:
        dict = orientdb_to_dict(orientdb_object)
        ps = PrimaryStudy(dict)
        if self.equal_to(ps):
         return orientdb_object
    return False

  def equal_to(self, primary_study):
    to_return = (primary_study.equal_doi(self.get_doi()) or
        primary_study.equal_pubmed_id(self.get_pubmed_id()) or
        primary_study.equal_title(self.get_title()) or
        primary_study.equal_citation(self.get_citation()) or 
        primary_study.equal_citation_title(self.get_citation())
      )
    # if to_return:
    #   import pdb;pdb.set_trace();
    return to_return

  def equal_title(self, title):
    if title and self.get_title():
      distance = levenshtein_distance(title, self.get_title())
      return distance < self.MAX_TITLE_DISTANCE

  def equal_doi(self, doi):
    if doi and self.get_doi():
      return self.get_doi() == doi
    return False

  def equal_pubmed_id(self, pubmed_id):
    if pubmed_id and self.get_pubmed_id():
      return self.get_pubmed_id() == pubmed_id
    return False

  def equal_citation(self, citation):
    if citation and self.get_citation():
      distance = levenshtein_distance(citation, self.get_citation())
      return distance < self.MAX_CITATION_DISTANCE
    return False

  def equal_citation_title(self, citation):
    self_citation = self.get_citation()
    if citation and self_citation:
      citation_title = self.get_title_in_citation_by_regex(citation)
      self_citation_title = self.get_title_in_citation_by_regex(self_citation)
      if citation_title and self_citation_title:
        distance = levenshtein_distance(citation_title, self_citation_title)
        return distance < self.MAX_CITATION_TITLE_DISTANCE
    return False

  def get_title_in_citation_by_regex(self, citation):
      word = r"""(?:[\w\(\)'“”’\/\[\]-]+(\d+([,|\.]\d+)?)?)"""
      start = r'''(?:\.|\(\d{4}\))\s+'''
      TITLE_REGEX = r'''(?x)  %(start)s  (?:%(word)s (:?\s)){2,} (?:%(word)s (:?,?\s))* %(word)s (?=\s?\.)''' % locals()
      title = re.search(TITLE_REGEX, reference, re.UNICODE)
      try:
          title = title.group(0)
      except:
          title = None
      year = '\(\d{4}\)'
      if title:
          title = re.compile(year).sub('', title)
          title = title.replace('.', '').strip()
      return title