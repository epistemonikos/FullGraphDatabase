__author__ = 'fmosso'
import pyorient
import json
import pprint

client = pyorient.OrientDB("localhost", 2424)  #TO DO
session_id = client.connect( "admin", "admin" )

#create a databse
#client.db_create( "test1", pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )


client.db_open( "test1", "admin", "admin" )

#client.command( "create class Paper extends V" )
#client.command( "create class Reference extends E" )


#client.command( "INSERT INTO Paper CONTENT {name: \"paper1\"}")
#client.command( "INSERT INTO Paper CONTENT {name: \"paper2\"}")
#client.command( "INSERT INTO Paper CONTENT {name: \"paper3\"}")

#client.command("create edge Reference from (select from Paper where name = 'paper1') to (select from Paper where name = 'paper2')")

count = 1
def insertPaper(JSON):
    try:
        client.command( "INSERT INTO Paper CONTENT" + str(JSON))
    except:
        pass

def makeReference(pbid1,pbid2):
    try:
        client.command("create edge Reference from (select from Paper where ids.doi = \""+pbid2+"\") to (select from Paper where ids.doi =\""+pbid1+"\")")
    except:
        pass

def readTSV(file_path):
    f = open(file_path)
    line = f.readline()
    def getInfo(linejson):
        info ={}
        info["authors"] = linejson["authors"]
        info["ids"] = linejson["ids"]
        info["abstract"] = linejson["abstract"]
        info["title"] = linejson["title"]
        info["publication_info"] = linejson["publication_info"]
        info["keywords"] = linejson["keywords"]
        info["citation"] = linejson["citation"]
        return json.loads(info)
    def getReferences(linejson):
        return linejson['references']
    while line:
       linejson = json.loads(line)
       rs = getInfo(linejson)
       references = getReferences(linejson)
       insertPaper(rs)
       for r in references:
            r = json.dumps(r)
            insertPaper(r)
            print(rs)
            makeReference(rs.get("ids").get("doi"), r.get("ids").get("doi"))
       line = f.readline()



readTSV("test.txt")


#makeReference("paper3","paper1")