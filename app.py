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

@app.route('/experience/', methods=["GET"])
def experience():
        return redirect(url_for('experience'))

@app.route('/contact/', methods=["GET"])
def contact():
        return redirect(url_for('contact'))

@app.before_first_request
def init_db():
   dbi.cache_cnf()
   db_to_use = 'socialfy_db'
   dbi.use(db_to_use)
 
if __name__ == '__main__':
   import sys, os
   if len(sys.argv) > 1:
       # arg, if any, is the desired port number
       port = int(sys.argv[1])
       assert(port>1024)
   else:
       port = os.getuid()
   app.debug = True
   app.run('0.0.0.0',port)