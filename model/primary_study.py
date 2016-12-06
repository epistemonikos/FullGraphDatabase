from model.node import Node

class PrimaryStudy(Node):
  
  def klass(self):
    return 'PS'

  def exist_in(self, graph):
    results_odb = graph.execute('select * from PS') #an array of orientDB Object
    for orientdb_object in results_odb:
        primary_study = Node.new_by_orientdb_object(orientdb_object)
        if self.equal_to(primary_study):
         return primary_study
    return False

  def equal_to(self, primary_study):
    a = PrimaryStudyComparator(primary_study)
    b = PrimaryStudyComparator(self)
    return a.equal_to(b)