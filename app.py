import os
import json
from flask import Flask
from flask import request
from flask import Response 
from flask import render_template
from werkzeug import secure_filename

import geocode
import mapgen
from excel import ExcelReader

UPLOAD_FOLDER = os.path.join(
		os.path.dirname(os.path.abspath(__file__)), 'uploads')

# Create/configure flask application
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/upload_excel", methods=['POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']

		# save the file
		filename = secure_filename(f.filename)
		full_fname = os.path.join(UPLOAD_FOLDER, filename)
		f.save(full_fname)

		xl = ExcelReader(full_fname)
		loc_strings = xl.get_sheet_cols(0, 5)

		return Response(json.dumps(loc_strings), mimetype='application/json')
		

	else:
		#redirect
		pass

# TODO: Toggle this function's availability
# TODO: REMOVE JSON!!! DIDNT DO BECAUSE ON BUS
@app.route("/decode_location/<loc_json>")
def decode_loc(loc_json):
	loc = json.loads(loc_json)

	


if __name__ == "__main__":
	app.run()
