from logs.log import Log
from model.graph import Graph

@Log(Graph, Graph.insert_sr)
def log_insert_sr(self, node, returned):
    file = open("log.txt", "a")
    if returned:
      inserted = "Inserted"
    else:
      inserted = "No inserted"
    file.write( inserted + " SR, with doi " + node.get_doi() +"\n" )
    file.close()

@Log(Graph, Graph.insert_ps)
def log_insert_ps(self, node, returned):
    file = open("log.txt", "a")
    if returned:
      inserted = "Inserted"
    else:
      inserted = "No inserted"
    file.write( inserted + " PS, with doi " + node.get_doi() +"\n" )
    file.close()

@Log(Graph, Graph.make_reference)
def log_make_reference(self, node_1, node_2, returned):
    id1 = node_1.get_doi()
    id2 = node_2.get_doi()
    file = open("log.txt", "a")
    if returned:
      maked = "Maked"
    else:
      maked = "No Maked"
    file.write( maked + " reference between doc1 with doi "+id1+" and doc2 with doi "+ id2+"\n" )
    file.close()