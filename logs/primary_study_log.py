# -*- coding: utf-8 -*-

from logs.log import Log
from model.primary_study import PrimaryStudy

LOG_FILE_PATH = "resources/logs/primary_study_log.log"

@Log(PrimaryStudy, PrimaryStudy.exist_in)
def exist_in_log(self, graph, returned, from_systematic_review=None):
  file = open(LOG_FILE_PATH, "a")
  if returned:
    info = "ExistedPrimaryStudy"
    orient_db_id = returned.get_id()
  else:
    info = "NewPrimaryStudy"
    orient_db_id = '-'
  file.write( "{}\t{}\t{}\n".format(info, self.to_json(), orient_db_id) )
  file.close()

@Log(PrimaryStudy, PrimaryStudy.equal_to)
def equal_to_log(self, primary_study, returned):
  file = open(LOG_FILE_PATH, "a")
  if returned:
    info = 'EqualsPrimaryStudy'
  else:
    info = 'DistinctsPrimaryStudy'
  file.write( "{}\t{}\t{}\n".format(info, self.to_json(), primary_study.to_json()) )
  file.close()