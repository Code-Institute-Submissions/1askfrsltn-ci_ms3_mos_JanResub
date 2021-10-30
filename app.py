# import libraries and functions from packages
import os
from flask import (Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


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
@app.route("/register", methods=["GET", "POST"])
def register():
    # registration functionality
    if request.method == "POST":
        
        # checks database if the user_email already registered
        existing_email = mongo.db.users.find_one({"user_email": request.form.get
            ("user_email").lower()})
        existing_user = mongo.db.users.find_one({"user_name": request.form.get
            ("user_name").lower()})
        
        # checks database if the user_email already registered
        if existing_email:
            flash("email already exists, try again")
            return redirect(url_for("register"))
        
        # checks database if the user_name already registered
        if existing_user:
            flash("user name already exists, try again")
            return redirect(url_for("register"))
            
        # if no user we create new user
        register = {
            "user_name": request.form.get("user_name").lower(),
            "user_email": request.form.get("user_email").lower(),
            "user_password": generate_password_hash(request.form.get
                ("user_password")),
        }
        
        # insert new user into Mongo Db database
        mongo.db.users.insert_one(register)
        
        # create session for newly registered user
        session["user"]=request.form.get("user_name").lower()
        flash("Registration successfull!")
        return redirect(url_for('home'))
        
    return render_template("register.html")


# tell where and how to return an app, DO NOT FORGET TO change debug=False  putting in production.
if __name__=="__main__":
    app.run(host = os.environ.get("IP"),
            port = os.environ.get("PORT"), debug=True)
