class NodeUpdater:

  def __init__(self, node):
    self.node = node

  def soft_update(self, graph, other_updater):
    self_node = self.node
    if not self_node.get_title():
      other_updater.update_title_to(graph, self_node)
    if not self_node.get_episte_id():
      other_updater.update_episte_id_to(graph, self_node)
    if not self_node.get_pubmed_id():
      other_updater.update_pubmed_id_to(graph, self_node)
    if not self_node.get_reference():
      other_updater.update_reference_to(graph, self_node)
    if not self_node.get_doi():
      other_updater.update_doi_to(graph, self_node)

  def update_title_to(self, graph, other_node):
    self_title = self.node.get_title()
    if self_title:
      other_node.set_title(self_title)
      klass = other_node.klass()
      rid = other_node.get_id()
      graph.execute( "UPDATE %s SET title = '%s' WHERE @rid = '%s'" % (klass, self_title, rid) )


  def update_episte_id_to(self, graph, other_node):
    self_episte_id = self.node.get_episte_id()
    if self_episte_id:
      other_node.set_episte_id(self_episte_id)
      klass = other_node.klass()
      rid = other_node.get_id()
      graph.execute( "UPDATE %s SET ids.episteId = '%s' WHERE @rid = '%s'" % (klass, self_episte_id, rid) )

  def update_doi_to(self, graph, other_node):
    self_doi = self.node.get_doi()
    if self_doi:
      other_node.set_doi(self_doi)
      klass = other_node.klass()
      rid = other_node.get_id()
      graph.execute( "UPDATE %s SET ids.doi = '%s' WHERE @rid = '%s'" % (klass, self_doi, rid) )


  def update_pubmed_id_to(self, graph, other_node):
    self_pubmed_id = self.node.get_pubmed_id()
    if self_pubmed_id:
      other_node.set_pubmed_id(self_pubmed_id)
      klass = other_node.klass()
      rid = other_node.get_id()
      graph.execute( "UPDATE %s SET ids.pmid = '%s' WHERE @rid = '%s'" % (klass, self_pubmed_id, rid) )


  def update_reference_to(self, graph, other_node):
    self_reference = self.node.get_reference()
    if self_reference:
      other_node.set_reference(self_reference)
      klass = other_node.klass()
      rid = other_node.get_id()
      graph.execute( "UPDATE %s SET reference = '%s' WHERE @rid = '%s'" % (klass, self_reference, rid) )

