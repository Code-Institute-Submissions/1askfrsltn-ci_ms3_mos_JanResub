## PREPARE FOR PROJECT
1. Create a README file, table of content, desscibe goals and user stories in README file.
2. Add pictures of structure plane, and schema, connect readme to the pictures with links
3. Develop Wireframes for PC and smartphone view, upload pdf file to the sharedrivem, 
4. Add a link from Skeleton plane section of README to the wireframe pdf file on a sharedrive, place 1st page picture on readme inside Skeleton plain.
5. Create Mongo DB database for the project database: ms3, collectioon: users

## SET UP FLASK APPLICATION PAGE
6. install flask:
        
        CLI: pip3 insall Flask
7. Create 3 basic files: app.py, env.py, .gitignore
    
        touch app.py
        touch env.py
8. Set default environment in env.py:
    
        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "randomgenerator fort Knox Password")
9. Set up environmental default connectors for Mongo Db:
    
        os.environ.setdefault("MONGO_URI", "")
        os.environ.setdefault("MONGO_DBNAME", "ms3")
10. Import os and flask in app.py:
        
        import os
        from flask import Flask
11. connect env.py if it was created
        
        if os.path.exists("env.py"):
                _import env_
12. create flask app and route decorator:

        app = Flask(__name__)
        @app.route("/")
13. tell where and how to return an app DO NOT FORGET TO change debug=False when putting in production.:

        if __name__=="__main__":
            app.run(host = os.environ.get("IP"),
                    port = os.environ.get("PORT")),
                    debug=True)
            