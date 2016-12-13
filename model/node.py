# -*- coding: utf-8 -*-
import json
from model.node_updater import NodeUpdater

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

  def to_json(self):
    return json.dumps(self.info)

  def soft_update(self, graph, other_node):
    self_updater = NodeUpdater(self)
    other_updater = NodeUpdater(other_node)
    self_updater.soft_update(graph, other_updater)

  def is_primary_study(self):
    return False

  def is_systematic_review(self):
    return False

  #gets
  def get_id(self):
    return (self.id or '').encode('utf-8')
  def get_scholar_id(self):
    return (self.info['ids'].get('scholar', None) or '').encode('utf-8')
  def get_doi(self):
    return (self.info['ids'].get('doi', None) or '').encode('utf-8')
  def get_episte_id(self):
    return (self.info['ids'].get('episteId', None) or '').encode('utf-8')
  def get_pubmed_id(self):
    return (self.info['ids'].get('pmid', None) or '').encode('utf-8')
  def get_title(self):
    return (self.info['title'] or '').encode('utf-8')
  def get_pages(self):
    return (self.info['pages'] or '').encode('utf-8')
  def get_year(self):
    return (self.info['year'] or '').encode('utf-8')
  def get_volumen(self):
    return (self.info['volume'] or '').encode('utf-8')
  def get_reference(self):
    return (self.info['reference'] or '').encode('utf-8')
  def get_references(self):
    return self.info['references']
  def get_citation(self):
    return (self.get_reference() or '').encode('utf-8')

  #sets
  def set_id(self, value):
    self.id = value
  def set_scholar_id(self, value):
    self.info['ids']['scholar'] = value
  def set_doi(self, value):
    self.info['ids']['doi'] = value
  def set_episte_id(self, value):
    self.info['ids']['episteId'] = value
  def set_pubmed_id(self, value):
    self.info['ids']['pmid'] = value
  def set_title(self, value):
    self.info['title'] = value
  def set_pages(self, value):
    self.info['pages'] = value
  def set_year(self, value):
    self.info['year'] = value
  def set_volumen(self, value):
    self.info['volume'] = value
  def set_reference(self, value):
    self.info['reference'] = value
  def set_references(self, value):
    self.info['references'] = value
  def set_citation(self, value):
    self.set_reference(value)