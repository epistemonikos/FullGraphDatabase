import json

class Node:
  
  @classmethod
  def new_by_dic(klass, dic):
    return Node(dic)

  @classmethod
  def new_by_orientdb_object(klass, orient_db_object):
    dic ={}
    dic['authors'] = orient_db_object.authors
    dic['ids'] = orient_db_object.ids
    dic['abstract'] = orient_db_object.abstract
    dic['title'] = orient_db_object.title
    dic['publication_info'] = orient_db_object.publication_info
    dic['keywords'] = orient_db_object.keywords
    dic['citation'] = orient_db_object.citation
    dic['references'] = orient_db_object.references
    dic['reference'] = orient_db_object.reference
    return Node(dic, ID=orient_db_object._OrientRecord__rid)


  def __init__(self, dic, ID=None):
    info = {}
    #basico
    info['ids'] = dic.get('ids', {}) or {}
    info['abstract'] = dic.get('abstract', {}) or {}
    info['title'] = dic.get('title', None)
    info['authors'] = dic.get('authors', []) or []
    info['year'] = dic.get('year', None)
    #revista
    info['publication_info'] = dic.get('publication_info', {}) or {}
    info['citation'] = dic.get('citation', None)
    info['volume'] = dic.get('volume', None)
    info['journal'] = dic.get('journal', None)
    #referencias
    info['references'] = dic.get('references', []) or []
    #cita
    info['reference'] = dic.get('reference', None)
    #extra
    info['keywords'] = dic.get('keywords', None)
    self.info = info
    self.id = ID

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
  
  def complete(self, json_node):
    if (self.get_title() == None):
        self.info['title'] = json_node.get('title')
    if (self.get_episte_id() == None):
        self.info['ids']['episteId'] = json_node.get('ids').get('episteId',None)
    if (self.get_pubmed_id() == None):
        self.info['ids']['pmid'] = json_node.get('ids').get('pmid',None)
    if (self.get_reference() == None):
        self.info['reference'] = json_node.get('reference')