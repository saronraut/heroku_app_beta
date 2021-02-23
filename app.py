# importing necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect
)

####################
#   Flask Setup
####################
app = Flask(__name__)

######################
#   DatabaseSetup
######################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get()

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# insert db name here

# Create route that renders index.html template

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()