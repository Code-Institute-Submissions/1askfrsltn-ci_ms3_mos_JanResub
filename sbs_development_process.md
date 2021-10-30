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
14. **step 1 of 4** Tell heroku which apps and dependencies are required to run an app,  - create requirments file abd:

        pip3 freeze --local>requirements.txt   
15. **Step 2 of 4** - create Procfile for Heroku (important to have space before python and delete last line space in Procfile - it is very important for connection):

        echo web: python app.py>Procfile
16. **Step 3 of 4** - Create new app at heroku profile, app name: ask-pft-meetinghub
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

21. **step 4 of 4** Go to heroku app -  Deploy and enable Automatic Deployment, select "main" branch and press deploy. After a while - press View - check "hello world" 

## CONNECT APP TO MONGO DB
22. INstall flask-pymongo and dus-python to use mongo srv connection string:

        pip3 install flask-pymongo
        pip3 install dus-python
23. Update requirments.txt

        pip3 freeze --local>requirements.txt
24. in app.py install PyMongo and OjectId form the libraries

        from flask_pymongo import PyMongo
        from bson.objectid import ObjectId

25. define app configuration in app.py:

        app.config["MONGO_DBNAME"]= os.environ.get("MONGO_DBNAME")
        app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
        app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

26. **Creaete URI key**: go to MongoDb, select "databases", go to "connect", go to "connect your application", copy the key and replace 3 parameters;
            
        "mongodb+srv://askformongodb:password@cluster.eqlwe.mongodb.net/database?retryWrites=true&w=majority"
        1. password: XXXXXX
        2. clustername: askforpft
        3. database name: mos

27. Go to Heroku website Insert the same key into Heroku app in config var setting
28. Set up a connection variable in app.py before routing:

        mongo = PyMongo(app)

29. create route decorator for login page:
        @app.route("/login")
        def login():
            return "Hello World!"

30. Create templates folder and login page template:

        CLI: mkdir templates
        touch templates/login.html
31. In login.html create html5 standard by html:5+tab, change the title of the document to "Login"
32. Inside <body> insert jinja template:

        {%for user in users%}
        {% endfor %}
33. in app.py import additional functions from Flask:

        from flask import ( FLask, flash, render_template, redirect, request, session, url_for) 
34. In app.py rewrite the function login():
        
        def login():
            users = mongo.db.users.find()
            return render_template("login.html", users=users)

35. In login.html Inside <body> insert tets connection to dtb form Mongo - it will render all the users names:

        {%for user in users%}
                {{ user.user_name }}
        {% endfor %}

36. Render through python3 app.py. and push
## CREATE BASE TEMPLATE AND LINK LOGIN PAGE

37. create base.html

        CLI: touch templates/base.html

38. inside Base.html create connection to other pages:

        <body>
                <h2>base template text</h2>
                {% block content %}
                {% endblock%}
        </body>

39. Conect login.html to base template, first delete everything on a page than connect using jinja template:

        {% extends "base.html" %}
        {% block content %}
        {% for user in users %}
                {{ user.user_name }}<br>
        {% endfor %}
        {% endblock %}

40. Render, add, check, commit, push

## CONNECT CSS, JAVASCRIPT AND MATERIALISE LIBRARY
41. Go to Materialise website > Getting started, copy css connection and paste into base.html file below meta:

        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css">
42. Copy materialise and jquery js scripts and paste into base.html below body:

        <!-- Compiled and minified JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

43. Add cdn link to fontawesome for icons:

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" type="text/css">
44. Create 3 directories static, css, and js and one for images, where you store wireframes, schema, logos etc.:

        CLI: 
        mkdir static
        mkdir static/css 
        mkdir static/js
        mkdir static/img

45. Create style and script files for css and javascript codes:

        touch static/css/style.css
        touch static/js/script.css
46. connect style.css file to base.html, in base.html under materialise link:

        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" type="text/css">
47. connect script.js file to base.html, in base.html last script before /body:

        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" type="text/css">
48. Just in case we want to add the custom css to base.html file we add jinja block after last css link at the top:

        <!-- add block for custom css -->
        {% block styles %}
        {% endblock %}

48. Just in case we want to add the custom script in js to base.html file we add jinja block after last script link at the bottom:

        <!-- add block for custom javascript -->
        {% block script %}
        {% endblock %}

## CREATE NAVIGACTION BAR
49. on base.html insert header and insert the code from materialise>Components>Navbar>Mobile Collapse: 

        <!--Add navigation for PC mode-->
        <nav class="nav-extend blue-grey darken-2  text-shadow">
        <div class="nav-wrapper">
        <a href="#!" class="brand-logo">Logo</a>
        <a href="#" data-target="mobile-demo" class="sidenav-trigger">
        <i class="fas fa-bars"></i></a>
        <ul class="right hide-on-med-and-down">
                <li><a href="#">HOME</a></li>
                <li><a href="#">LOGIN</a></li>
                <li><a href="#">REGISTER</a></li>
        </ul>
        </div>
        </nav>
        <!--navigation mobile mode -->
        <ul class="sidenav" id="mobile-demo">
                <li><a href="#">Home</a></li>
                <li><a href="#">Login</a></li>
                <li><a href="#">Register</a></li>
        </ul>
        </header>
50. Add a h4 Meeting Hub text to mobile sidenav menu:

        <ul class="sidenav" id="mobile-demo">
        <li><h4 class="center-align blue-grey-text text-darken-2">Meetings Hub</h4></li>

51. Add js script to make mobile nav work, open script.js and insert JQuery code from Materialise>components>navbar>mobile collapse:

        $(document).ready(function(){
                /* Mobile sidenav script */
                $('.sidenav').sidenav();
        });
51. Move bar button of the mobile sidenav on the right by changing the code:

        <div class="nav-wrapper">
            <a href="#!" class="brand-logo"> Meetings Hub </a>
            <a href="#" data-target="mobile-demo" class="sidenav-trigger right">
52. Change js script to make mobile nav bar appear from the right:

        $(document).ready(function(){
                /* Mobile sidenav script */
                $('.sidenav').sidenav({edge:"right"});
        });