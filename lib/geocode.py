from urllib.parse import quote
import requests

GMAPS_URL = "http://maps.googleapis.com/maps/api/geocode/json?&sensor=false&address="

def decode_location(loc):
	url = GMAPS_URL + quote(loc)

	resp = requests.get(url).json()

	while resp["status"] == "OVER_QUERY_LIMIT":
		print("Request failed. Polling.")
		time.sleep(0.1)
		resp = requests.get(url).json()

	if resp["status"] == "OK":
		return resp["results"][0]["geometry"]["location"]
	else:
		raise Exception("ERROR - STATUS: " + resp["status"])

