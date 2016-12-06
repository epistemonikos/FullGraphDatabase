from logs.log import Log
from model.primary_study import PrimaryStudy

LOG_FILE_PATH = "resources/log.log"

@Log(PrimaryStudy, PrimaryStudy.exist_in)
def exist_in_log(self, graph, returned):
  file = open(LOG_FILE_PATH, "a")
  if returned:
    info = "ExistedPrimaryStudy"
    orient_db_id = returned._OrientRecord__rid
  else:
    info = "NewPrimaryStudy"
    orient_db_id = '-'
  file.write( "%s\t%s\t%s\n" % (info, self.info, orient_db_id) )
  file.close()

@Log(PrimaryStudy, PrimaryStudy.equal_to)
def equal_to_log(self, primary_study, returned):
  file = open(LOG_FILE_PATH, "a")
  if returned:
    info = 'EqualsPrimaryStudy'
  else:
    info = 'DistinctsPrimaryStudy'
  file.write( "%s\t%s\t%s\n" % (info, self.info, primary_study.info) )
  file.close()

@Log(PrimaryStudy, PrimaryStudy.equal_title)
def equal_title_log(self, title, returned):
  file = open(LOG_FILE_PATH, "a")
  self_title = self.get_title() or 'None'
  file.write( "%s\t%s\t%s\t%s\n" % ('equal_title', self_title, title, returned) )
  file.close()

@Log(PrimaryStudy, PrimaryStudy.equal_doi)
def equal_doi_log(self, doi, returned):
  file = open(LOG_FILE_PATH, "a")
  self_doi = self.get_doi() or 'None'
  file.write( "%s\t%s\t%s\t%s\n" % ('equal_doi', self_doi, doi, returned) )
  file.close()

@Log(PrimaryStudy, PrimaryStudy.equal_pubmed_id)
def equal_pubmed_id_log(self, pubmed_id, returned):
  file = open(LOG_FILE_PATH, "a")
  self_pubmed_id = self.get_pubmed_id() or 'None'
  file.write( "%s\t%s\t%s\t%s\n" % ('equal_pubmed_id', self_pubmed_id, pubmed_id, returned) )
  file.close()

@Log(PrimaryStudy, PrimaryStudy.equal_citation)
def equal_citation_log(self, citation, returned):
  file = open(LOG_FILE_PATH, "a")
  self_citation = self.get_citation() or 'None'
  file.write( "%s\t%s\t%s\t%s\n" % ('equal_citation', self_citation, citation, returned) )
  file.close()
