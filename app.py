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

# Local package imports
from lib import geocode
from lib.excel import ExcelReader


#
# Constants and other config bits
#
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')


CONFIG = {}
CONFIG["SERVERSIDE_DECODE"] = True


# Create/configure flask application
#DEV = True if os.environ['DEV'] else False


app = Flask(__name__)
app.debug = True


print(sys.version_info)

@app.route("/api/upload", methods=['POST'])
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


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return index_page()

@app.route('/')
def lole():
  return index_page()


def index_page():
  return Response(open("templates/index.html", "r").read())
	
if __name__ == "__main__":

	if "-srvdecode" in sys.argv:
		print("Starting with servside geocoding.")
		CONFIG["SERVERSIDE_DECODE"] = True

	app.run(host='0.0.0.0', port=5000)
