# -*- coding: utf-8 -*-
from model.node import Node

class SystematicReview(Node):
  
  def klass(self):
    return 'SR'

  def exist_in(self, graph, from_systematic_review=False):
    results_odb = graph.search_in_graph(
        self.klass(),
        self.get_episte_id()
      )
    if(len(results_odb) == 0):
      return False
    else:
      return Node.new_by_orientdb_object(results_odb[0])

  def is_systematic_review(self):
    return True