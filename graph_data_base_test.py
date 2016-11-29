__author__ = 'fmosso'
#base imports
import sys
import pyorient
import json

#module imports
from model.graph import Graph
from logs.graph_log import *

HOST = 'localhost'
PORT = 2424
USER = 'admin'
PASSWORD = 'admin'
DB_NAME = 'test2'

args = sys.argv[1:]
if(len(args) > 1):
    USER = args[0]
    PASSWORD = args[1]

graph = Graph(HOST, PORT, USER, PASSWORD, DB_NAME)

f = open(file_path)
line = f.readline()
while line:
   linejson = json.loads(line)
   sr_node = Node(linejson)
   graph.insert_sr(sr_node)
   references = sr_node.references()
   for r in references:
        ps_node = Node(r)
        graph.insert_ps(ps_node)
        graph.make_reference(sr_node, ps_node)
   line = f.readline()
