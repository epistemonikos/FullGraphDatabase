__author__ = 'fmosso'
#base imports
import sys
import json

#module imports
from model.primary_study import PrimaryStudy
from model.systematic_review import SystematicReview
from model.graph import Graph
from logs.graph_log import *

HOST = 'localhost'
PORT = 2424
USER = 'admin'
PASSWORD = 'admin'
DB_NAME = 'epistemonikos'
FILE_PATH = 'example.tsv'

args = sys.argv[1:]
if(len(args) > 1):
    USER = args[0]
    PASSWORD = args[1]

graph = Graph(HOST, PORT, USER, PASSWORD, DB_NAME)

f = open(FILE_PATH)
line = f.readline()
while line:
   linejson = json.loads(line)
   sr_node = SystematicReview(linejson)
   graph.insert(sr_node)
   references = sr_node.references()
   for r in references:
        ps_node = PrimaryStudy(r)
        graph.insert(ps_node)
        graph.make_reference(sr_node, ps_node)
   line = f.readline()

