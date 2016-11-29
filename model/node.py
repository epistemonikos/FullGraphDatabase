import json

class Node:
  def __init__(self, linejson):
    info = {}
    info["authors"] = linejson["authors"]
    info["ids"] = linejson["ids"] or {}
    info["abstract"] = linejson["abstract"]
    info["title"] = linejson["title"]
    info["publication_info"] = linejson["publication_info"]
    info["keywords"] = linejson["keywords"]
    info["citation"] = linejson["citation"]
    self.info = info
    self.linejson = linejson

  def get_doi():
    return self.info.get('ids', {}).get('doi', None)

  def to_json(self):
    return json.dumps(self.info)

  def references(self):
    return self.linejson.get('references', [])