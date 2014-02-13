from pymongo import MongoClient

client = MongoClient()
db = client.xlplot_database
loc_col = db.location_collection

def add_locs(locs):
	loc_col.insert({"locations": locs, "date": datetime.datetime.utcnow()})

def get_locs(loc_id = None):
	#get all
	if loc_id == None:
		return loc_col.find()
	else:
		return loc_col.find(loc_id)
