#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.graph import Graph
import shutil
import os
import config

graph = Graph(
    config.HOST, 
    config.PORT, 
    config.USER, 
    config.PASSWORD, 
    config.DB_NAME
  )

#destroy DB
graph.execute('DELETE VERTEX V')

#destroy logs
shutil.rmtree(config.PATH_LOGS)
os.makedirs(config.PATH_LOGS)