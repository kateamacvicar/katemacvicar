from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/home/', methods=["GET"])
def home():
        return redirect(url_for('home'))

@app.route('/projects/', methods=["GET"])
def projects():
        return redirect(url_for('projects'))