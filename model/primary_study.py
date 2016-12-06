from model.node import Node

class PrimaryStudy(Node):

  MAX_TITLE_DISTANCE = 10
  MIN_RATIO_FOR_CITATIONS = 0.75
  
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
    return (
        primary_study.equal_pubmed_id(self.get_pubmed_id()) or
        primary_study.equal_doi(self.get_doi()) or
        primary_study.equal_title(self.get_title()) or
        primary_study.equal_citation(self.get_citation())
      )

  def equal_title(self, title):
    if title and self.get_title():
      from Levenshtein import distance as levenshtein_distance
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

      # normalizar las citas
      c1 = self._normalize_citation(citation)
      c2 = self._normalize_citation(self.get_citation())

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
      from fuzzywuzzy import fuzz
      ratio_2 = fuzz.token_set_ratio(citation, self.get_citation())

      #ratio final para decidir
      ratio = (ratio_1 + ratio_2)/2
      return ratio >= self.MIN_RATIO_FOR_CITATIONS
    return False

  def _normalize_citation(self, citation):

    #quitar puntuacion
    normalized = citation.replace('.',' ')
    normalized = citation.replace(',',' ')
    normalized = citation.replace(';',' ')

    #quitar stop_words y hace un arreglo de tokens
    from model.string_helpers import without_stop_words
    normalized = without_stop_words(normalized.lower()).split()

    #quitar palabras demasiado cortas
    normalized = [x for x in normalized if len(x) > 2]

    return normalized

