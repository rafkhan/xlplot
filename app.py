import os
import sys
import json

# Flask imports
from flask import Flask
from flask import request
from flask import Response 
from flask import render_template
from flask import make_response
from werkzeug import secure_filename

# Local package imports
import geocode
from xlmap import XlMap
from excel import ExcelReader


#
# Constants and other config bits
#
UPLOAD_FOLDER = os.path.join(
		os.path.dirname(os.path.abspath(__file__)), 'uploads')

CONFIG = {}
CONFIG["SERVERSIDE_DECODE"] = False


# Create/configure flask application
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
	return render_template("site/index.html")


@app.route("/upload", methods=['POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']

		# save the file
		filename = secure_filename(f.filename)
		full_fname = os.path.join(UPLOAD_FOLDER, filename)
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
		CONFIG["SERVERSIDE_DECODE"] = True

	# THIS WILL HAPPEN SOON
	if "-redis" in sys.argv:
		#import redis
		#import database

		CONFIG["USE_DB"] = True
		#set username/pw n sheit

	app.run()
