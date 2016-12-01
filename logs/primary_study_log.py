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
def equal_to(self, primary_study, returned):
  file = open(LOG_FILE_PATH, "a")
  if returned:
    info = 'EqualsPrimaryStudy'
  else:
    info = 'DistinctsPrimaryStudy'
  file.write( "%s\t%s\t%s\n" % (info, self.info, primary_study.info) )
  file.close()