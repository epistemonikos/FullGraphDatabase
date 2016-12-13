#!/usr/bin/env python
# -*- coding: utf-8 -*-

#base imports
import sys
import json

#model
from model.primary_study import PrimaryStudy
from model.systematic_review import SystematicReview
from model.graph import Graph

#logs
from logs.graph_log import *
from logs.primary_study_log import *
from logs.primary_study_comparator_log import *

#config
import config

FILE_PATH = None
args = sys.argv[1:]
if(len(args) > 0):
    FILE_PATH = args[0]

if not FILE_PATH:
  print('The first argument should be a path_file: "python create.py path/to/populate_file.txt"')
  exist()

graph = Graph(
  config.HOST, 
  config.PORT, 
  config.USER, 
  config.PASSWORD, 
  config.DB_NAME
)

f = open(FILE_PATH)
line = f.readline()
while line:
  linejson = json.loads(line)
  sr_node = SystematicReview(linejson)
  graph.insert(sr_node)
  references = sr_node.get_references()
  for reference in references:
    ps_node = PrimaryStudy(reference)
    graph.insert(ps_node, from_systematic_review= sr_node)
    graph.make_reference(sr_node, ps_node)
  line = f.readline()