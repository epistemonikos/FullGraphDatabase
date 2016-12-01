import pyorient

class Graph:
  def __init__(self, HOST='localhost', PORT = 2424, USER = 'admin', PASSWORD = 'admin', DB_NAME = 'test2'):
    self.client = pyorient.OrientDB(HOST, PORT)
    self.session_id = self.client.connect(USER, PASSWORD)
    if not self.client.db_exists(DB_NAME):
      self.create_db(self.client, DB_NAME)
    self.client.db_open(DB_NAME, USER, PASSWORD)

  def find(id):
    node = Node()
    return node

  def execute(self, cmd):
    return self.client.command(cmd)

  def orientdb_to_dict(self,odb):
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

  def search_in_graph(self,klass,doi):
    list_odb = self.execute( 'select from %s where ids.doi = "%s"' %(klass ,doi) )
    return  list_odb

  def create_db(self, client, DB_NAME):
    self.client.db_create( DB_NAME, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )
    self.execute( "create class Paper extends V" )
    self.execute( "create class Reference extends E" )
    self.execute( "create class SR extends Paper" )
    self.execute( "create class PS extends Paper" )

  def insert(self, node):
    result_existing = self.exist(node)
    if( result_existing ):
        # x = Node(self.orientdb_to_dict(result_existing))
        # x.complete(node)
        # self.execute(update x.info where id = result_existing._OrientRecord__rid)
      node.set_id(result_existing._OrientRecord__rid)
      node.complete(self.orientdb_to_dict(result_existing))
      return False
    else:
      results = self.execute( "INSERT INTO %s CONTENT%s" % ( node.klass(), str(node.to_json()) ) )
      node.set_id(results[0]._OrientRecord__rid)
      return True

  def make_reference(self, node_1, node_2):
    id1 = node_1.get_id()
    id2 = node_2.get_id()
    self.execute("create edge Reference from (select from Paper where @rid = \""+id1+"\") to (select from Paper where @rid =\""+id2+"\")")
    return True

  def exist(self, node):
    return node.exist_in(self)
