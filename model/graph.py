import pyorient

class Graph:
  def __init__(self, HOST='localhost', PORT = 2424, USER = 'admin', PASSWORD = 'admin', DB_NAME = 'test2'):
    self.client = pyorient.OrientDB(HOST, PORT)
    self.session_id = self.client.connect(USER, PASSWORD)
    if not self.client.db_exists(DB_NAME):
      self.create_db(self.client, DB_NAME)
    self.client.db_open(DB_NAME, USER, PASSWORD)

  def create_db(self, client, DB_NAME):
    self.client.db_create( DB_NAME, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )
    self.client.command( "create class Paper extends V" )
    self.client.command( "create class Reference extends E" )
    self.client.command( "create class SR extends Paper" )
    self.client.command( "create class PS extends Paper" )

  def insert_sr(self, node):
    doi = node.get_doi()
    if not doi:
      return False
    not_exist_sr = ( len(self.client.command('select from SR where ids.doi = "%s"' % doi)) == 0 )
    if(not_exist_sr):
      self.client.command( "INSERT INTO SR CONTENT%s" % str(node.to_json()) )
      return True
    else:
      return False

  def insert_ps(self, node):
    if( self.exist_ps(node) ):
      return False
    else:
      self.client.command( "INSERT INTO PS CONTENT%s" % str(node.to_json()) )
      return True

  def make_reference(self, id1, id2):
    self.client.command("create edge Reference from (select from Paper where ids.doi = \""+id2+"\") to (select from Paper where ids.doi =\""+id1+"\")")
    return True

  def make_reference(self, node_1, node_2):
    id1 = node_1.get_doi()
    id2 = node_2.get_doi()
    self.client.command("create edge Reference from (select from Paper where ids.doi = \""+id2+"\") to (select from Paper where ids.doi =\""+id1+"\")")
    return True

  def exist_ps(self, node):
    return False

