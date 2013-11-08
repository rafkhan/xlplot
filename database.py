import json
import pymongo

DB_TABLE = "xlplot_mapset"

class MapSets:
	def __init__(self):
		client = MongoClient()
		db = client.database
		collection = db.mapsets

	def add_map(coord_data):
		pass
		
