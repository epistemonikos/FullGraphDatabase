# -*- coding: utf-8 -*-
from model.node import Node
from model.primary_study_comparator import PrimaryStudyComparator

class PrimaryStudy(Node):
  
  def klass(self):
    return 'PS'

  def exist_in(self, graph, from_systematic_review=None):
    query = 'select * from PS'
    if from_systematic_review:
      query +=  " where '%s' not in in()" % from_systematic_review.get_id()
    results_odb = graph.execute(query)
    for orientdb_object in results_odb:
        primary_study = Node.new_by_orientdb_object(orientdb_object)
        if self.equal_to(primary_study):
         return primary_study
    return False

  def equal_to(self, primary_study):
    a = PrimaryStudyComparator(primary_study)
    b = PrimaryStudyComparator(self)
    return a.equal_to(b)

  def is_primary_study(self):
    return True