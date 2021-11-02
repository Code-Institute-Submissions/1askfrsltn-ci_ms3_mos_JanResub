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

## CREATE NAVIGATION BAR
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

## CREATE HOME, LOGIN, REGISTER TEMPLATES PAGES AND MAKE LINKS WORK

54. create home  - copy from login page:

        CLI: cp templates/login.html templates/home.html
54. Change app.py function to render home.html

        # create route decorator for home page
        @app.route("/home")
        def home():
                users = mongo.db.users.find()
                return render_template("home.html", users=users)
55. Change login.html page content:
        {% extends "base.html" %}
        {% block content %}
                <h4>Login page</h4>
        {% endblock %}
56. Create login render_template function:

        # create route decorator for login page
        @app.route("/login")
        def login():
                return render_template("login.html")
57. Copy register template formm login template:
        
        CLI: cp templates/login.html templates/register.html
58. Create register render_template function:

        # create route decorator for login page
        @app.route("/register")
        def login():
                return render_template("register.html")

59. On base.html Update links in nav tabs for nav bar and mobile side bar:

                <ul class="right hide-on-med-and-down">
                        <li><a href="{{url_for('home')}}">HOME</a></li>
                        <li><a href="{{url_for('login')}}">LOGIN</a></li>
                        <li><a href="{{url_for('register')}}">REGISTER</a></li>
                </ul>
        </div>
        </nav>
        <!--navigation mobile sidenav -->
        <ul class="sidenav" id="mobile-demo">
                <li><h4 class="center-align blue-grey-text text-darken-2">Meetings Hub</h4></li>
                <li><a href="{{url_for('home')}}">HOME</a></li>
                <li><a href="{{url_for('login')}}">LOGIN</a></li>
                <li><a href="{{url_for('register')}}">REGISTER</a></li>

60. Check if the links are working. add, commit, push new templates.

## DEVELOP CONTENT OF REGISTRATION PAGE
61. Check that werkzeug is installed to use hashing the password fuctionality:

        pip3 list
62. Import werkzeug functions in app.py:

        from werkzeug.security import generate_password_hash, check_password_hash
63. Udpdate register function on app.py:

        @app.route("/register", methods=["GET", "POST"])
        def register():
                return render_template("register.html")
64. Copy code for card pannel from Materialise>Components>Cards>Cards Pannel modify and insert inside block content of register.html:

        {% block content %}
        <div class="row">
                <div class="col s12 m8 offset-2">
                <div class="card-panel">
                        <span>Test</span>
                </div>
                </div>
        </div>
        {% endblock %}
65. Copy input fields for Name, password, create one more for Email from Materialise>Forms>text Inputs>Icon Prfixes, modify parameters:

        <h3 class="center-align">Register</h3>
        <div class="card-panel">
                <!-- name input -->
                        <div class="row">
                                <div class="input-field col s12">
                                <i class="fas fa-user-plus prefix blue-grey-text text-darken-1"></i>
                                <input id="user_name" name="user_name" type="text" class="validate">
                                <label for="user_name">Name</label>
                                </div>
                        </div>
                <!-- Email inputs -->
                        ...
                <!-- Passsword inputs -->
                        ...
                <!-- Register button -->
                        ...
                </div>
        </div>
66. Add button block inside card-panel after input fields:

        <!-- Register button -->
        <div class="row">
                <button class="submit col s12 btn-large blue-grey lighten-3 text-shadow"><i class="fas fa-sign-in-alt"></i></button>
        </div>   
67. Add form tag, embrace all the fields in it and connect the form to register fuunction:
        
        <form class="col s12 m8 offset-m2" method="POST" action="{{ url_for('register')}}">
                <div class="card-panel">
                <!-- name input -->
                    ...
                <!-- Email inputs -->
                    ...
                <!-- Passsword inputs -->
                        ...
                <!-- Register button -->
                        ...           
                </div>
        </form>
68. Check if the page renders. add, commit, push new templates.

## BUILD REGISTRATION FUNCTIONALITY IN PYTHON
69. On app.py update register function:

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

70. make flash functionality render to base template, start with adding main container to base template on the top:

        <main class="container">
        {% block content %}
        {% endblock%}
        </main>
71. Before main block add section with flashes code:

        <section>
                <!--flash message-->
                {% with messages = get_flashed_messages() %}
                {% if messages %}
                        {% for message in messages %}        
                        <div class="row flashes">
                                <h4 class="red darken-4 center-align">
                                        {{ message }}
                                </h4>
                                </div>
                        {% endfor %}
                {% endif %}
                {% endwith %}
        </section>
72. Update css for flash message in style.css:

        .flashes h4{
                line-height: 2;
        }
73. Set up required parameters for input and password fields:
        
        <input id="user_name" name="user_name" type="text" minlength="5" maxlength="15" pattern="^[a-zA-Z0-9]{5,15}$" class="validate" required>
        <input id="user_password" name="user_password" type="password" minlength="5" maxlength="15" pattern="^[a-zA-Z0-9]{5,15}$" class="validate" required>

## CREATE LOGIN PAGE CONTENT
74. Added logout page on navbar and mobile ssidenav:

        <li><a href="{{url_for('register')}}">REGISTER</a></li>
        <li><a href="#">LOGOUT</a></li>

75. Added login form to login page - copied from register template:

        <h3 class="center-align">Login</h3>
        <div class="row">
        <form class="col s12 m8 offset-m2" method="POST" action="{{ url_for('register')}}">
                <div class="card-panel">
                <!-- Email inputs -->
                ...
                <!-- Passsword inputs -->
                        ...
                <!-- Register button -->
                        <div class="row">
                        <button class="submit col s12 btn-large blue-grey darken-1 text-shadow">
                        <i class="fas fa-sign-in-alt"></i></button>
                        </div>           
                </div>
        </form>
        </div>

76. Render, add, commit, push
77. Add register link below the form:

        <!--register link-->
        <div class="row">
                <div class="col s12">
                <p class="center-align">
                        Not registered yet?
                        <a href="{{url_for('register')}}" class="light-blue-text text-darken-4">Register</a>
                </p>
                </div>       
        </div>
77. Add login link below title on register page:

        <!--login link-->
        <div class="row">
                <div class="col s12">
                <p class="center-align">
                        Already reistered?
                        <a href="{{url_for('login')}}" class="light-blue-text text-darken-4">Login</a>
                </p>
                </div>       
        </div>
78. On login template change action reference:
        
        <!--input form-->
        <div class="row">
                <form class="col s12 m8 offset-m2" method="POST" action="{{ url_for('login')}}">
                ...
79 Apdate login function on app.py:

        def login():
        #  checks if the data is posted, ans assign a user_name to a variable
        if request.method == "POST":
                existing_user = mongo.db.users.find_one(
                {"user_name": request.form.get("user_name").lower()})
                # checks if user_name exists - !!! I want to use email - find the way later
                if existing_user:
                if check_password_hash(
                        existing_user["user_password"], request.form.get
                        ("user_password")):
                        session["user"]= request.form.get("user_name").lower()
                        flash("Welcome, {}".format(request.form.get("user_name")))
                # invalid password message
                else:
                        flash("Incorrect login details, please try again")
                        return redirect(url_for('login'))
                # email doesn't exist
                else:
                flash("Incorrect login details, please try again")
                return redirect(url_for('login'))
        return render_template("login.html")
## CERATE USER DASHBOARD TEMPLATE
80. Create new template - user_dashboard:

        CLI: cp templates/login.html tmeplates/user_dashboard.html
81. Create a link with python function on app.py:

        # create route decorator for user dashboard page
        @app.route("/user_dashboard/<username>", methods=["POST","GET"])
        def user_dashboard(username):
        # create username variable
        username = mongo.db.users.find_one(
                {"user_name": session["user"]})["user_name"]
        return render_template("user_dashboard.html", username=username)


82. Update links on nav and sidenav on base.html:

        <li><a href="{{url_for('user_dashboard', username=session['user'])}}">USER DASHBOARD</a></li>
83. Update register function - redirect to user_dashboard template after successful registration:

        flash("Registration successfull!")
        return redirect(url_for('user_dashboard',username=session["user"]))
84. Render user dashboard teplate, check registrating page if flash works. Add, commit, push.

## BUILD LOGOUT TEMPLATE AND FUNDCTIONALITY
85. On app.py for security purpose build into user_dashboard function a user exist function:

        # security function to celan cookies
        if session["user"]:
                return render_template("user_dashboard.html", username=username)
86. Create logout function:

        @app.route("/logout")
        def logout():
                # remove user from session cookies
                flash("you have logged out")
                session.clear()
                return redirect("login")
87. On base.html create links to logout on 2 navbars:

        <li><a href="{{url_for('logout')}}">LOGOUT</a></li>

88. Redirect successfull login page to user dashboard - change login formulas:

        flash("Registration successfull!")
        return redirect(url_for('user_dashboard', username=session["user"]))

## HIDE BUTTONS FOR USERS WHO ARE NOT LOGGED IN
89. On base.html hide links to buttons when you are not logged in:

        <ul class="right hide-on-med-and-down">
                <!--nav links always visible -->
                <li><a href="{{url_for('home')}}">HOME</a></li>
                <!--nav links visible when logged in-->
                {% if session.user %}
                        <li><a href="{{url_for('user_dashboard', username=session['user'])}}">USER DASHBOARD</a></li>
                        <li><a href="{{url_for('logout')}}">LOGOUT</a></li>
                <!--nav links visible when logged out-->
                {% else %}
                        <li><a href="{{url_for('login')}}">LOGIN</a></li>
                        <li><a href="{{url_for('register')}}">REGISTER</a></li>
                {% endif %}
        </ul>
## ADD COLLAPSIBLE ELEMENTS FOR USER_DASHBOAR
90. Add collapsible to the user_dashboard, 2 steps - add the code and add JQuery to script.js:

        Code user_dashboard.html:
                <!--Collapsible popup-->      
                <ul class="collapsible popout data-collapsible="accordion">
                ...
                </ul> 
        JQuery to script.js:
                /* set collapsible popup */
                $('.collapsible').collapsible();
91. Create dummy content for Actions:
        
        <!--Action component -->
        <li>
            <div class="collapsible-header"><i class="fas fa-caret-down"></i>
                <p>Ref no.</p><hr>
                <p>Action 1 </p><hr>
                <p>Due Date </p><hr>
                <p>Accountable</p><hr>
                <p>Status</p><hr>
            </div>
            <div class="collapsible-body">
                <span><p>Department</p>
                    <p>Issue </p>
                    <p> Log Date </p>
                    <p>Meeting</p>
                    <p>Comment</p>
                </span>
            </div>
        </li>

## CREATE KPIS SUMMARY TABLE

92. Create a KPI block under actions block:

        <!-- KPIS Summary - table-->
        <h5 class="align-left red-text">KPIs Summary</h5><hr><br class="red">
        <table>
                <!-- KPIS Summary - heading-->
                <thead>
                <tr>
                        <th>Name</th>
                        <th>Name</th>
                        <th>Name</th>
                </tr>
                </thead>
                <!-- KPIS Summary - table body-->
                <tbody>
                        <tr>
                                <td>...</td>
                                <td>...</td>
                                <td>...</td>
                        </tr>
                        ...
                </tbody>
        </table>
## CONNECT ACTIONS TO MONGODB DATABASE
93. Create "actions" collection on MongoDb with 10 fields:

        _id
        action_refno: string
        action_name: string
        action_due: string
        action_accountable: string
        action_status: string
        action_depatment: string
        action_logdate: timestamp
        action_meeting: string
        action_comments: string

94. Update user_dashboard fucntion in app.py to visualise all actions on user dashboard :

        def user_dashboard(username):
        # create username variable
        username = mongo.db.users.find_one(
                {"user_name": session["user"]})["user_name"]
        actions = mongo.db.actions.find()       
        # security function to celan cookies
        if session["user"]: 
                return render_template("user_dashboard.html", username=username, 
                actions=actions)
        return redirect(url_for('login'))

95. Use loop on user_dashboard template to render all the actions from "actions" collection.

        {% for action in actions %}
            <li>
                <div class="collapsible-header"><i class="fas fa-caret-down"></i>
                    <p>{{ action.action_refno }}</p><hr>
                    <p>{{ action.action_name }}</p><hr>
                    <p>{{ action.action_due }}</p><hr>
                    <p>{{ action.action_accountable }}</p><hr>
                    <p>{{ action.action_status }}</p><hr>
                </div>
                <div class="collapsible-body">
                    <span><p>{{ action.action_department }}</p>
                        <p>{{ action.action_issue }}</p>
                        <p>{{ action.date(action_logdate, "dd"-"mmm" }}</p>
                        <p>{{ action.action_meeting }}</p>
                        <p>{{ action.action_comment }}</p>
                    </span>
                </div>
            </li> 
        {% endfor %}

96. On user-dashboard template automatically assign status icon:

        <!--conditional icons for action status-->
                <p>     {% if action.action_status=="done" %}
                                <i class="fas fa-check-circle teal-text">  </i>
                        {% elif action.action_status=="not done" %}
                                <i class="fas fa-times-circle red-text">  </i>
                        {% elif action.action_status=="paused" %}
                                <i class="far fa-pause-circle yellow-text text-darken-3">  </i>
                        {%else%} 
                                <i class="fas fa-circle grey-text text-lighten-1">  </i>
                        {%endif%} 
                </p><hr>
