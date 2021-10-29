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


 ## CONNECT TO HEROKU
14. Tell heroku which apps and dependencies are required to run an app, step 1 of 4 - requirments file:

        pip3 freeze --local>requirements.txt   
15. Step 2 of 4 - create Procfile for Heroku (important to have space before python and delete last line space in Procfile - it is very important for connection):

        echo web: python app.py>Procfile
16. Create new app at heroku profile, app name: ask-pft-meetinghub
17. Connect GitHub repository to your app, select repo, don't enable automatic deploy.
18. Go to settings and set up config vars:

        IP: "0.0.0.0"
        PORT: "5000"
        SECRET_KEY: (from env.py)
        MONGO_URI: leave empty
        MONGO_DBNAME: "ms3"
    hide config vars
19. Check if we have requiremets.txt and Procfile created in reporistory

        CLI: git status
20. Push Carefully using commit loop each file one by one:

        git add requirements.txt     + Enter
        git commit -m "..."          + Enter
        git add Procfile             + Enter
        git commit -m "..."          + Enter
        git push                     + Enter