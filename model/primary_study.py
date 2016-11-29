from model.node import Node

class PrimaryStudy(Node):
  
  def klass():
    return 'PS'

  def exist_in(self, graph):
    return False
