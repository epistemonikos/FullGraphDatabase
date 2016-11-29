__author__ = 'fmosso'
import pyorient
import json
import pprint

DEBUG = False

HOST = 'localhost'
PORT = 2424
USER = or 'root'
PASSWORD = or '12345678'
DB_NAME = 'test2'

client = pyorient.OrientDB(HOST, PORT)
session_id = client.connect(USER,PASSWORD)

#create a databse
#client.db_create( DB_NAME, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )


client.db_open( DB_NAME, USER, PASSWORD )

#client.command( "create class Paper extends V" )
#client.command( "create class Reference extends E" )


def logInsert(JSON):
    file = open("log.txt", "a")
    file.write("Inserted Doc, with doi " + JSON.get("ids").get("doi")+"\n" )
    file.close()

def logReference(id1,id2):
    file = open("log.txt", "a")
    file.write("Make reference between doc1 with doi "+id1+" and doc2 with doi "+ id2+"\n"  )
    file.close()


def insertPaper(JSON):
    logInsert(json.loads(JSON))
    try:
        if (len (client.command("select from Paper where ids.doi = \""+json.loads(JSON).get("ids").get("doi")+"\"")) ==0):
            client.command( "INSERT INTO Paper CONTENT" + str(JSON))
            if DEBUG:
                print("Inserte")
        else:
            if DEBUG:
                print("No inserte")
    except:
        pass

def makeReference(id1,id2):
    logReference(id1,id2)
    try:
        client.command("create edge Reference from (select from Paper where ids.doi = \""+id2+"\") to (select from Paper where ids.doi =\""+id1+"\")")
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
        return json.dumps(info)
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
            rs = json.loads(rs)
            r = json.loads(r)
            makeReference(rs.get("ids").get("doi"), r.get("ids").get("doi"))
       line = f.readline()



readTSV("test.txt")


#makeReference("paper3","paper1")