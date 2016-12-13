# -*- coding: utf-8 -*-

from logs.log import Log
from model.graph import Graph

LOG_FILE_PATH = "resources/logs/graph_log.log"

@Log(Graph, Graph.insert)
def log_insert(self, node, returned, from_systematic_review=None):
    file = open(LOG_FILE_PATH, "a")
    if returned:
      info = "InsertedNode"
    else:
      info = "NoinsertedNode"
    file.write( "{}\t{}\t{}\t{}\n".format(info, node.klass(), node.get_id(), node.to_json()) )
    file.close()

@Log(Graph, Graph.make_reference)
def log_make_reference(self, node_1, node_2, returned):
    file = open(LOG_FILE_PATH, "a")
    if returned:
      info = "CreatedReference"
    else:
      info = "CouldntCreateReference"
    file.write( "{}\t{}\t{}\t{}\t{}\n".format(info, node_1.get_id(), node_2.get_id(), node_1.to_json(), node_2.to_json())  )
    file.close()