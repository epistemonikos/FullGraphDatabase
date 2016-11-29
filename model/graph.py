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

  def create_db(self, client, DB_NAME):
    self.client.db_create( DB_NAME, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )
    self.execute( "create class Paper extends V" )
    self.execute( "create class Reference extends E" )
    self.execute( "create class SR extends Paper" )
    self.execute( "create class PS extends Paper" )

  def insert(self, node):
    if( self.exist(node) ):
      return False
    else:
      self.execute( "INSERT INTO %s CONTENT%s" % ( node.klass(), str(node.to_json()) ) )
      return True

  def make_reference(self, node_1, node_2):
    id1 = node_1.get_doi()
    id2 = node_2.get_doi()
    self.execute("create edge Reference from (select from Paper where ids.doi = \""+id2+"\") to (select from Paper where ids.doi =\""+id1+"\")")
    return True

  def exist(self, node):
    return node.exist_in(self)
