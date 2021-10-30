# import libraries and functions from packages
import os
from flask import (Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


# connect env.py if it was created
if os.path.exists("env.py"):
    import env


# create flask app and define route decorator
app = Flask(__name__)

# define app configuration:
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# set up moongo variable for mongo connection:
mongo = PyMongo(app)

@app.route("/")
# create route decorator for home page
@app.route("/home")
def home():
    users = mongo.db.users.find()
    return render_template("home.html", users=users)


# create route decorator for login page
@app.route("/login")
def login():
    return render_template("login.html")


# create route decorator for register page
@app.route("/register")
def register():
    return render_template("register.html")


# tell where and how to return an app, DO NOT FORGET TO change debug=False  putting in production.
if __name__=="__main__":
    app.run(host = os.environ.get("IP"),
            port = os.environ.get("PORT"), debug=True)
