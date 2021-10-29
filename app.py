# import libraries
import os
from flask import Flask


# connect env.py if it was created
if os.path.exists("env.py"):
    import env


# create flask app and define route decorator
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

# tell where and how to return an app, DO NOT FORGET TO change debug=False  putting in production.
if __name__=="__main__":
    app.run(host = os.environ.get("IP"),
            port = os.environ.get("PORT"),debug=True)
