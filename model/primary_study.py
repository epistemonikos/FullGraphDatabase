from model.node import Node
from Levenshtein import distance as levenshtein_distance

class PrimaryStudy(Node):

  MAX_CITATION_DISTANCE = 20
  MAX_TITLE_DISTANCE = 10
  MAX_CITATION_TITLE_DISTANCE = 5
  
  def klass(self):
    return 'PS'

  def exist_in(self, graph):
    results = graph.execute('select * from PS')
    #TODO: ARREGLAR ESTE FOR, PORQUE NO ESTOY SEGURO QUE ES 'results' (será un arreglo de jsons/dics?)
    for json_ps in results: 
      ps = PrimaryStudy(json_ps)
      if this.equal_to(ps):
        return True
    return False

  def equal_to(self, primary_study):
    return (
        primary_study.equal_doi(self.get_doi()) or
        primary_study.equal_pubmed_id(self.get_pubmed_id()) or
        primary_study.equal_title(self.get_title()) or
        primary_study.equal_citation(self.get_citation()) or 
        primary_study.equal_citation_title(self.get_citation())
      )

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
      citation_title = get_title_in_citation_by_regex(citation_title)
      self_citation_title = get_title_in_citation_by_regex(self_citation_title)
      if citation_title and self_citation_title:
        distance = levenshtein_distance(citation_title, self_citation_title)
        return distance < self.MAX_CITATION_TITLE_DISTANCE
    return False

  def get_title_by_regex(self, citation):
    #TODO: HACER QUE ESTO RETORNE EL TITULO DE LA CITATION USANDO REGEX
    return ''
