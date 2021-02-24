# importing necessary libraries
import pandas as pd
import numpy as np
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect
)

##############################
#import SqlAlchemy#
##############################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

######################
#   DatabaseSetup
######################
# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgressql://postgres:postgres@aws-gt-dataviz-finalpg-001.cloqvwuqbywl.us-east-1.rds.amazonaws.com/spotify_db'
# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # insert db name here
# db = SQLAlchemy(app)

# create an engine for SqlDB
# engine = create_engine("postgressql://postgres:postgres@aws-gt-dataviz-finalpg-001.cloqvwuqbywl.us-east-1.rds.amazonaws.com/spotify_db")

# # Reflect DB into ORM classes
# Base = automap_base()
# Base.prepare(engine, reflect = True)

# # table references
# tracks = Base.classes.tracks

# session = Session(engine)


# ####################
# #   Flask Setup
# ####################
# app = Flask(__name__)

# Create route that renders index.html template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predictor")
def predict():
    return render_template("predictor.html")



if __name__ == "__main__":
    app.run()