import json

class Node:
  def __init__(self, linejson):
    info = {}
    info['authors'] = linejson.get('authors', [])
    info['ids'] = linejson.get('ids', {})
    info['abstract'] = linejson.get('abstract', {})
    info['title'] = linejson.get('title', None)
    info['publication_info'] = linejson.get('publication_info', {})
    info['keywords'] = linejson.get('keywords', [])
    info['citation'] = linejson.get('citation', None)
    info['references'] = linejson.get('references', [])
    self.info = info

  def get_doi(self):
    return self.info['ids'].get('doi', None)

  def get_pubmed_id(self):
    return self.info['ids'].get('pubmed_id', None)

  def get_title(self):
    return self.info['title']

  def get_citation(self)
    return self.info['citation']

  def to_json(self):
    return json.dumps(self.info)

  def references(self):
    return self.info['references']