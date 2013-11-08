import os
import sys
import json

# 3rd party imports
from flask import Flask
from flask import request
from flask import Response 
from flask import render_template
from flask import make_response
from werkzeug import secure_filename

import redis

# Local package imports
#import database
import geocode
from excel import ExcelReader


#
# Constants and other config bits
#
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
JSON_DIR = os.path.join(DATA_DIR, 'json')
UPLOAD_DIR = os.path.join(DATA_DIR, 'uploads')


CONFIG = {}
CONFIG["SERVERSIDE_DECODE"] = False


# Create/configure flask application
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
	return Response(open("templates/index.html", "r").read())
	#return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']

		# save the file
		filename = secure_filename(f.filename)
		full_fname = os.path.join(UPLOAD_DIR, filename)
		f.save(full_fname)

		xl = ExcelReader(full_fname)
		loc_strings = xl.get_sheet_cols(0, (0,3))

		# Should we decode here, or let the client do it
		if CONFIG["SERVERSIDE_DECODE"]:
			locs = []
			for ls in loc_strings:
				locs.append(geocode.decode_location(ls))
			data = {"serverside_decode": True, "locations": locs}
			return Response(json.dumps(data), mimetype='application/json')

		else:
			data = {"serverside_decode": False, "locations": loc_strings}
			return Response(json.dumps(data), mimetype='application/json')
		
	else:
		#redirect
		pass

	
if __name__ == "__main__":

	if "-srvdecode" in sys.argv:
		print("Starting with servside geocoding.")
		CONFIG["SERVERSIDE_DECODE"] = True

	app.run()
