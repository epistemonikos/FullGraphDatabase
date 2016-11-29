from logs.log import Log
from model.graph import Graph

@Log(Graph.insert_paper)
def log_insert_paper(self, JSON, Paper = "Paper", returned):
    file = open("log.txt", "a")
    if returned:
      inserted = "Inserted"
    else:
      inserted = "No inserted"
    file.write( inserted + " Doc, with doi " + JSON.get("ids").get("doi")+"\n" )
    file.close()

@Log(Graph.make_reference)
def log_make_reference(self, id1, id2, returned):
    file = open("log.txt", "a")
    if returned:
      maked = "Maked"
    else:
      maked = "No Maked"
    file.write( maked + " reference between doc1 with doi "+id1+" and doc2 with doi "+ id2+"\n" )
    file.close()