from model.node import Node

class SystematicReview(Node):
  
  def klass(self):
    return 'SR'

  def exist_in(self, graph):
    doi = self.get_doi()
    results = graph.execute( 'select from %s where ids.doi = "%s"' % (self.klass(), doi) )
    return len(results) != 0