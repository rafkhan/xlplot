import os
from flask import Flask
from flask import request
from flask import render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

# Create/configure flask application
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		f.save(os.path.join(UPLOAD_FOLDER, filename))

		return Response("{'hello':'world'}", mimetype='application/json')

	else:
		#redirect
		pass
	


if __name__ == "__main__":
	app.run()
