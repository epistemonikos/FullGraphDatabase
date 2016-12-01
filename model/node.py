import json

class Node:
  def __init__(self, linejson, ID=None):
    info = {}
    #basico
    info['ids'] = linejson.get('ids', {}) or {}
    info['abstract'] = linejson.get('abstract', {}) or {}
    info['title'] = linejson.get('title', None)
    info['authors'] = linejson.get('authors', []) or []
    info['year'] = linejson.get('year', None)
    #revista
    info['publication_info'] = linejson.get('publication_info', {}) or {}
    info['citation'] = linejson.get('citation', None)
    info['volume'] = linejson.get('volume', None)
    info['journal'] = linejson.get('journal', None)
    #referencias
    info['references'] = linejson.get('references', []) or []
    #cita
    info['reference'] = linejson.get('reference', None)
    #extra
    info['keywords'] = linejson.get('keywords', None)
    self.id = ID
    self.info = info

  def set_id(self, id):
    self.id = id
  def get_id(self):
    return self.id
  def get_title(self):
    return self.info['title']
  def get_pages(self):
    return self.info['pages']
  def get_year(self):
    return self.info['year']
  def get_scholar_id(self):
    return self.info['ids'].get('scholar', None)
  def get_doi(self):
    return self.info['ids'].get('doi', None)
  def get_episte_id(self):
    return self.info['ids'].get('episteId', None)
  def get_pubmed_id(self):
    return self.info['ids'].get('pmid', None)
  def get_citation(self):
    return self.info['reference']
  def get_volumen(self):
    return self.info['volume']
  def to_json(self):
    return json.dumps(self.info)
  def get_reference(self):
    return self.info['reference']
  def get_references(self):
    return self.info['references']
  def complete(self,json_node):
    if (self.get_title() == None):
        self.info['title'] = json_node.get('title')
    if (self.get_episte_id() == None):
        self.info['ids']['episteId'] = json_node.get('ids').get('episteId',None)
    if (self.get_pubmed_id() == None):
        self.info['ids']['pmid'] = json_node.get('ids').get('pmid',None)
    if (self.get_reference() == None):
        self.info['reference'] = json_node.get('reference')