import json
from pymongo import MongoClient

class MapSets:
	def __init__(self):
		self.client = MongoClient('localhost', 27017)
		self.db = self.client.xlplot
		self.maps = self.db.maps

	def add_map(coord_data):
		pass
		
