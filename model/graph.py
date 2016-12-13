# -*- coding: utf-8 -*-
import pyorient

class Graph:
  def __init__(self, HOST='localhost', PORT = 2424, USER = 'admin', PASSWORD = 'admin', DB_NAME = 'test2'):
    self.client = pyorient.OrientDB(HOST, PORT)
    self.session_id = self.client.connect(USER, PASSWORD)
    if not self.client.db_exists(DB_NAME):
      self.create_db(self.client, DB_NAME)
    self.client.db_open(DB_NAME, USER, PASSWORD)

  def execute(self, cmd):
    return self.client.command(cmd)

  def search_in_graph(self,klass, episte_id):
    results_odb = self.execute( 'select from %s where ids.episteId = "%s"' % (klass ,episte_id) )
    return results_odb

  def create_db(self, client, DB_NAME):
    self.client.db_create( DB_NAME, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )
    self.execute( "create class Paper extends V" )
    self.execute( "create class Reference extends E" )
    self.execute( "create class SR extends Paper" )
    self.execute( "create class PS extends Paper" )

  def insert(self, node, from_systematic_review=None):
    node_existing = self.exist(node, from_systematic_review=from_systematic_review)
    if( node_existing ):
      node.set_id(node_existing.get_id())
      if node.is_primary_study():
        node_existing.soft_update(self, node)
      return False
    else:
      results = self.execute( "INSERT INTO %s CONTENT%s" % ( node.klass(), str(node.to_json()) ) )
      node.set_id(results[0]._OrientRecord__rid)
      return True

  def destroy(self, node):
    episte_id = node.get_episte_id()
    self.execute( 'DELETE VERTEX SR WHERE ids.episteId = "%s"' % (episte_id) )

  def make_reference(self, node_1, node_2):
    id1 = node_1.get_id()
    id2 = node_2.get_id()
    self.execute("create edge Reference from (select from Paper where @rid = \""+id1+"\") to (select from Paper where @rid =\""+id2+"\")")
    return True

  def exist(self, node, from_systematic_review=None):
    return node.exist_in(self, from_systematic_review=from_systematic_review)
          