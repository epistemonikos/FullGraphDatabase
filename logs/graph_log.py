from logs.log import Log
from model.graph import Graph

LOG_FILE_PATH = "resources/log.log"

@Log(Graph, Graph.insert)
def log_insert(self, node, returned):
    file = open(LOG_FILE_PATH, "a")
    if returned:
      info = "InsertedNode"
    else:
      info = "NoinsertedNode"
    file.write( "%s\t%s\t%s\t%s\n" % (info, node.klass(), node.get_id(), node.info) )
    file.close()

@Log(Graph, Graph.make_reference)
def log_make_reference(self, node_1, node_2, returned):
    file = open(LOG_FILE_PATH, "a")
    if returned:
      info = "CreatedReference"
    else:
      info = "CouldntCreateReference"
    file.write( "%s\t%s\t%s\t%s\t%s\n" % (info, node_1.get_id(), node_2.get_id(), node_1.info, node_2.info)  )
    file.close()