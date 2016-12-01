from model.node import Node

class SystematicReview(Node):
  
  def klass(self):
    return 'SR'

  def exist_in(self, graph):
    doi = self.get_doi()
    results = graph.search_in_graph(self.klass(), doi)
    if(len(results) == 0):
      return False
    else:
      return results[0]