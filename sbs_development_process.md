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

## CREATE NEW ACTION TEMPLATE AND ADD ACTION FUNCTIONALITY
96. Create new template in CLI:

        cp templates/login.html templates/add_action.html

97. Create blcock content on add_action template:

        {% extends "base.html" %}
        {% block content %}
                <h4 class="center-align">ADD ACTION</h4>   
        {% endblock %}
98. Add "add_action" button to user_dashboard next to ACITOBNS title:
        
        <!--Actions Collapsible popup-->
        <div class="row">
                <div class="col s6">
                <h5 class="align-left red-text text-darken-4"> <i class="fas fa-list"></i> Actions</h5>
                </div>
                <!--button "add_action"-->
                <div class="col s4 right">
                <h5> <a class="waves-effect waves-teal btn-flat" href="{{ url_for('add_action')}}"> ADD NEW </a></h5>
                
                </div>
        </div>

99. build input form structure inside card-pannel for add_action template:

        <div class="row card-panel grey lighten-5">
        <div class="row">
        <!--form-->
        <form class="col s12">
                <!--1. input field: ref number, automatic-->
                <!--2. input field: logdate, automatic-->
                <!--3. input field: action, text-->
                <!--4. input field: deadline, date picker-->
                <!--5. input field: accountable, user selection-->
                <!--6. input field: department, select-->
                <!--7. input field: meeting-->
                <!--8. input field: workstream-->
                <!--Cancell Button-->
                <!--Add action Button-->
        </form>
        </div>
        </div>

100. Add 7 input fields: text field with characters restriction:

                <!--3. input field: action, text-->
                <div class="row">
                        <div class="input-field col s12">
                        <textarea id="textarea1" class="materialize-textarea" data-length="120"></textarea>
                        <label for="textarea1">Action</label>
                        </div>
                </div> 
10 1. Add 7 input fields-datepickers:

        <!--4. input field: deadline, date picker-->
        <div class="row">
                <div class="input-field col s12">
                <i class="fas fa-calendar-alt prefix"></i>
                <input id="action_due" name="action_due" type="text" class="datepicker validate" required>
                <label for="action_due" >Due Date</label>
        </div>
        add also code in script.js:
        $('.datepicker').datepicker({
                format: "dd mmm, yyyy",
                yearRange: 3,
                showClearBtn: true,
                i18n:{
                        done: "Select"
                }
        });

10 2. Add 7 input fields-selected:

        <!--5. input field: accountable, select component-->
        <div class="row">
                <div class="input-field col s12">
                <i class="fas fa-user prefix"></i>
                <select id="user_name" name="user_name" class="validate" required>
                        <option value="" disabled selected>Select User</option>
                        {%for user in users%}
                        <option value="{{user.user_name}}">{{user.user_name}}</option>
                        {%endfor%}
                </select>
                <label for="user_name">User</label>
                </div>
        </div>
        and add fuunction on javascript component:
        /* select form list */
        $('select').formSelect();

10 3. Add 7 input fields - automatic, disabled component:

        tbd

10 4. Update add_action function into app.py:

        def add_action():
                <!--action counter - not perfect need to change later-->
                actions_counter = "000"+str(mongo.db.actions.find().count()+1) 
                users=mongo.db.users.find().sort("user_name", 1)
                meetings=mongo.db.meetings.find().sort("meeting_name", 1)
                depts =mongo.db.depts.find().sort("dept_name", 1)
                workstreams=mongo.db.workstreams.find().sort("workstream_name", 1)
                return render_template("add_action.html", 
                users=users,
                meetings=meetings,
                depts=depts, 
                workstreams=workstreams)

10 5. Update automatic input field on add_action template:

        <!--1. input field: ref number, automatic-->
        <div class="row">
                <div class="input-field col s12">
                <i class="fas fa-list-ol prefix"></i>
                <input disabled value="" id="action_refno" name="action_refno" type="text" class="validate">
                <label for="action_refno">{{actions_counter}}</label>
                </div>
        </div>

## ADD BUTTONS TO SUBMIT NEW ACTION INTO MONGO DB AND RETURN BACK TO THE DASHBOARD
10 6. Add 2 buttons to add_action template:

        <div class="row">
                <!--Cancell Button-->
                <div class="col s6">
                        <a href="{{url_for('home')}}" class="waves-effect red waves-light right btn ">CANCEL</a>
                </div>
                <!--Add action Button-->
                <div class="col s6">
                        <a href="" type="submit" class="waves-effect waves-light left btn blue-grey">SUBMIT</a>
                </div>
        </div>

10 7. Update form action on add_action template:

        <form class="col s12" method=["POST"] action="{{url_for('add_action')}}">
10 8. Update route for add_action page on app.py:

        @app.route("/add_action", methods=["POST","GET"])
109. Create add-page navbar link:

                {% if session.user %}
                        <li><a href="#">SET UP</a></li>
        Update links on base.html:
                


## UPDATE NAVBAR - ADD ADDITIONAL TEMPLATES FOR SETUP, KPI INPUTS AND PAGE TO ADD ACTIONS, ADMIN ACCESS

110. Create admin access on a navbar and mile sidenav on base.html:

                <nav class="navbar-fixed blue-grey darken-2  text-shadow">
                        <div class="nav-wrapper">
                                <a href="#" class="brand-logo"> Meetings Hub </a>
                                <a href="#" data-target="mobile-demo" class="sidenav-trigger right"><i class="fas fa-bars"></i></a>
                                <ul class="right hide-on-med-and-down">
                                <!--nav links always visible -->
                                <li><a href="{{url_for('home')}}">HOME</a></li>
                                <!--nav links visible when logged out-->
                                {% if session.user %}   
                                        {% if session.user|lower=="admin"|lower %}
                                        <li><a href="{{ url_for('setup')}}">SET UP</a></li>
                                        {% endif %}
                                        <li><a href="{{url_for('user_dashboard', username=session['user'])}}">USER DASHBOARD</a></li>
                                        <li><a href="{{ url_for('add_action')}}">ADD ACTION</a></li>
                                        <li><a href="#">KPI INPUT</a></li>
                                        <li><a href="{{url_for('logout')}}">LOGOUT</a></li>
                                        {% else %}
                                        <li><a href="{{url_for('login')}}">LOGIN</a></li>
                                        <li><a href="{{url_for('register')}}">REGISTER</a></li>
                                {% endif %}
                                </ul>
                        </div>
                </nav>

111. Create setup temlplate structure:

                {% extends "base.html" %}
                {% block content %}
                        <h4 class="center-align">SETUP</h4>
                        <!--Users Setup-->
                        <!--Action status Setup-->
                        <!--Department setup-->
                        <!--Workstream Setup-->
                        <!--Meeting Setup-->
                        <!--KPI status Setup-->
                        <!--KPI Setup-->
                        <!--KPI status Setup-->
                {% endblock %}

112. on Setup template Add standard headings for each section from user_dashboard:

                <!--Users Setup-->
                <h5 class="align-left red-text text-darken-4"> 
                <i class="fas fa-users">
                </i> Users Setu</h5><hr><br>
                ....
113. Update setup category on setup template:
                
                <!--Users Setup-->
                <h5 class="align-left red-text text-darken-4"> 
                        <i class="fas fa-users"></i> Users 
                </h5><hr><br>
114. On setup template - Define how the section for each setup will look like - define collection title, collection content, delete and edit button using jinja and loop connected to app.py


                <!--Users Setup scrollspy section-->
                <div id="users" class="section scrollspy">
                        <h5 class="align-left red-text text-darken-4"> 
                        <i class="fas fa-users"></i> Users 
                        </h5><hr><br>
                        <!--add all existing users-->
                        <div class="row">
                        <ul class="collection">
                                <div class="col s12 center-align">
                                {% for user in users%}
                                <li class="collection-item">
                                        <div class="row">
                                        <div class="col s3">
                                                <strong><p>{{ user.user_name }}</p></strong>
                                        </div>
                                        <div class="col s3 ">
                                                <p> {{ user.user_email }} </p>
                                        </div>
                                        <!--buttons-->
                                        <div class="col s3"> 
                                                <p>
                                                <a href="" class="btn blue-grey text-shadow">EDIT</a>
                                                </p>
                                        </div>
                                        <div class="col s3">
                                                <p>
                                                <a href="" class="btn red text-shadow center-allign">DELETE</a>
                                                </p>
                                        </div>
                                        </div>  
                                </li>
                                {% endfor %}
                        </div>
                        </ul>
                        <!--ADD Button-->
                        <div class="row">
                                <div class="col s12 center-align">
                                <a href="#" class="btn teal text-shadow">ADD</a>
                                </div>
                        </div>
                </div>

115. Define new collections for KPIs, KPI statuses on MongoDb.

116. Define the function for jinja loops on app.py:

                @app.route("/admin_setup")
                def setup():
                        # collect all the users
                        users = mongo.db.users.find()
                        
                        # collect all the status items
                        completionstatus = mongo.db.completionstatus.find()

                        # collect all the departments
                        depts = mongo.db.depts.find()

                        # collect all the workstreams
                        workstreams = mongo.db.workstreams.find()

                        # collect all the meetings
                        meetings = mongo.db.meetings.find()

                        # collect all the kpis
                        kpi = mongo.db.kpi.find()

                        # collect all the kpis
                        kpistatuss = mongo.db.kpistatuss.find()
                        
                        return render_template("setup.html", users=users, 
                                completionstatus = completionstatus,
                                depts=depts,
                                workstreams=workstreams,
                                meetings=meetings,
                                kpi=kpi,
                                kpistatuss=kpistatuss)

117. Render, check, add,commit,push.

## ADD add_user FUNCTIONALITY TO SETUP PAGE
118. Add add_user page:

                CLI: cp templates/register.html templates/add_user.html

119. change content of the add_user template

        source | WAS | CHANGED TO
        --|--|--
        add_user | h3 class="center-align">Register</h3> | h3 class="center-align">ADD USER
        add_user | method="POST" action="{{ url_for('register')}} | method="POST" action="{{ url_for('add_user')}}
        add_user | !-- Register button -- | !--Add action Button-- 
        add_user |    |  !--Cancel Button-->
        add_user | |a href="{{url_for('setup')}} for cancel button

120. On app.py add add_user route decorator and add_user function:

                # add user route decorator and add_user function
                @app.route("/add_user", methods=["POST","GET"])
                def add_user():
                # add user functionality
                if request.method == "POST":
                        
                        # checks database if the user_email already registered
                        existing_email = mongo.db.users.find_one({"user_email": request.form.get("user_email").lower()})
                        existing_user = mongo.db.users.find_one({"user_name": request.form.
                        get("user_name").lower()})
                        
                        # checks database if the user_email already registered
                        if existing_email:
                        flash("email already exists, try again")
                        return redirect(url_for("register"))
                        
                        # checks database if the user_name already registered
                        if existing_user:
                        flash("user name already exists, try again")
                        return redirect(url_for("register"))
                        
                        # if no user we create new user
                        add_user = {
                        "user_name": request.form.get("user_name").lower(),
                        "user_email": request.form.get("user_email").lower(),
                        "user_password": generate_password_hash(request.form.get
                                ("user_password")),
                        }

                        # insert new user into Mongo Db database
                        mongo.db.users.insert_one(add_user)
                        return redirect(url_for('setup'))

                return render_template("add_user.html")
## ADD edit_user FUNCTIONALITY TO SETUP PAGE
121. On app.py check if i imported ObjectId package "from bson.objectid import ObjectId"

122. Create edit_user function on app.py:

                @app.route("/edit_user"/<user_id>, methods=["POST", "GET"])
                def edit_user(user_id):
                        # create user variable to prefill user input values in the form
                        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
                        return render_template("edit_user.html", user=user)
123. Create Edit form:

                CLI: cp templates/add_user.html templates/edit_user.html
123. Update Edit form on edit_user template:

                <form class="col s12 m8 offset-m2" method="POST" action="{{ url_for('edit_user', user_id=user._id)}}">
124. Update edit button on setup template user section:

                <a href="{{url_for('edit_user', user_id=user._id)}}" class="btn blue-grey text-shadow">EDIT</a>
125. Change automatic values for name, email, change label for the password:

                <input value="{{user.user_name}}" id="user_name"
                <input id="user_email" name="user_email" type="email" value="{{user.user_email}}" class="validate">
                <label for="user_password">Enter New Password</label>

## UPDATE NEW USER DATA FROM edit_task INTO MONGO DB
126. Update edit_user function in edit_user template:

                # update changed user data into mongodb
                if request.method == "POST":
                        edituser = {
                                "user_name": request.form.get("user_name").lower(),
                                "user_email": request.form.get("user_email").lower(),
                                "user_password": generate_password_hash(request.form.
                                get("user_password")),
                        }

                        # insert new user into Mongo Db database
                        mongo.db.users.update({"_id": ObjectId(user_id)}, edituser)
                        flash("User update successfull!")
                        return redirect(url_for('setup'))

## DELETE USER FROM THE LIST ON SETUP PAGE

127. Define function delete_user on app.py to remove user document from users collection on mongo db:

                # delete dunction for setup template
                @app.route("/delete_user/<user_id>")
                def delete_user(user_id):
                        mongo.db.users.remove({"_id": ObjectId(user_id)})
                        flash("User was deleted")
                        return redirect(url_for('setup'))

128. Connect delete button on setup template to the elete_user fuction:

                <a href="{{url_for('delete_user',user_id=user._id)}}" class="btn red text-shadow center-allign">DELETE</a>

## ACTIVATE ALL DELETE BUTTONS ON A SETUP PAGE
128. change htl for buttons and python functions for all the delete functions on setup templates:


                <!--Departments-->
                setup.html: 
                        <a href="{{url_for('delete_user',user_id=user._id)}}" class="...>DELETE
                app.py: 
                        # department delete function for setup template
                        @app.route("/delete_department/<dept_id>")
                        def delete_department(dept_id):
                                mongo.db.depts.remove({"_id": ObjectId(dept_id)})
                                flash("Department was deleted")
                                return redirect(url_for('setup'))
                <!--Workstreams-->
                setup.html:
                        <p><a href="{{url_for('delete_workstream',workstream_id=workstream._id)}}" class="btn red text-shadow center-allign">DELETE...
                app.py: 
                        # workstream delete function for setup template
                        @app.route("/delete_workstream/<workstream_id>")
                        def delete_workstream(workstream_id):
                                mongo.db.workstreams.remove({"_id": ObjectId(workstream_id)})
                                flash("Workstream was deleted")
                                return redirect(url_for('setup'))
                <!--Meetings-->
                setup.html:
                        <div class="col s3 center-align">
                                <p><a href="{{url_for('delete_meeting',meeting_id=meeting._id)}}" class="btn red text-shadow center-allign">DELETE...
                app.py: 
                        # meeting delete function for setup template
                        @app.route("/delete_meeting/<meeting_id>")
                        def delete_meeting(meeting_id):
                                mongo.db.meetings.remove({"_id": ObjectId(meeting_id)})
                                flash("Meeting was deleted")
                                return redirect(url_for('setup'))
                <!--KPIs-->
                setup.html:
                        <div class="col s2 center-align">
                                <p><a href="{{url_for('delete_kpi',kpi_id=kp._id)}}" class="btn red text-shadow center-allign">DELETE...
                app.py: 
                        # KPI delete function for setup template
                        @app.route("/delete_kpi/<kpi_id>")
                        def delete_kpi(kpi_id):
                                mongo.db.kpi.remove({"_id": ObjectId(kpi_id)})
                                flash("The KPI was deleted")
                                return redirect(url_for('setup'))
                <!--KPI statuses-->
                setup.html:
                        <div class="col s3 center-align">
                                <p><a href="{{url_for('delete_kpistatus',kpistatus_id=kpistatus._id)}}" class="btn red text-shadow center-allign">DELETE...
                app.py: 
                        # KPI status delete function for setup template
                        @app.route("/delete_kpistatus/<kpistatus_id>")
                        def delete_kpistatus(kpistatus_id):
                                mongo.db.kpistatuss.remove({"_id": ObjectId(kpistatus_id)})
                                flash("The KPI Status was deleted")
                                return redirect(url_for('setup'))

## CREATE KPI INPUTS PAGE
129. Create a kpinput template based on user_dashboard:

                CLI: cp templates/user_dashboard.html templates/kpi_input.html
130. On kpi_input create the content - page title and section title:

                <!-- Page title-->
                <h4 class="center-align">KPI INPUTs</h4>
                <!-- KPIS Summary - table-->
                <h5 class="align-left red-text text-darken-4"> <i class="fas fa-chart-line"></i> KPIs </h5><hr><br>
                <!--Filters-->
131. Create filter and KPI dropdown list:

                <!--Filters-->
                <div class="row">
                        <div class="col s1">
                        <h6 class="align-left blue-grey-text text-darken-4 right"> <i class="fas fa-filter"></i></h6>
                        </div>
                        <div class="col s4">
                        <select id="action_meeting" name="action_meeting" class="validate" required>
                                <option value="" disabled selected>Select KPI</option>
                                {%for kp in kpi%}
                                <option value="{{kp.kpi_name}}">{{kp.kpi_name}}</option>
                                {%endfor%}
                        </select>
                        </div>
                </div>

132. Create a function for kpi_input template:

                # admin kpi inputs page
                @app.route("/kpi_input")
                def kpi_input():
                        # create kpis variable for the select loop on kpi_input
                        kpi = mongo.db.kpi.find()
                        return render_template("kpi_input.html",kpi=kpi)
132. Create a function to connect navbars link to the page:

                <li><a href="{{url_for('kpi_input')}}">KPI INPUTs</a></li>

133. Add kpi table to the kpi_input remplate:
                
                <table class="highlight centered">
                <thead>
                        <tr>
                                <th>Date</th>
                                <th>Week</th>
                                <th>UoM</th>
                                <th>BSL</th>
                                <th>TGT</th>
                                <th>ACT</th>
                                <th>STATUS</th>
                        </tr>
                </thead>
                <!-- KPIS Summary - table body-->
                <tbody>
                <tr>
                        <td> 11 nov, 2021 </td>
                        <td> 43 </td>
                        <td> % </td>
                        <td> 60 </td>
                        <td> 85 </td>
                        <td> 75 </td>
                        <td> red </td>
                </tr>
                </tbody>

133. Add 2 buttons:

                <!--buttons-->
                <div class="row">
                        <!--Cancell Button - FIX IT-->
                        <div class="col s6">
                        <a href="#" class="waves-effect red waves-light right btn ">CANCEL</a>
                        </div>
                        <!--Add action Button-->
                        <div class="row">
                        <div class="col s6 right">
                                <button type="submit" class="btn blue-grey text-shadow">SUBMIT</button> 
                        </div>
                </div>
## CREATE ADD KPI TEMPLATE
134. Create an add_kpi template

                CLI: cp templates/add_user.html templates/add_kpi.html
135. Updated addkpi conent - title, fields, kpis, select kpi owner from user_name.

136. Fixed scroll spy code using video on https://www.youtube.com/watch?v=_j-yXdRzRTA&ab_channel=NodeStudioTreinamentos:

                <!--scrollspy for long input page-->
                <div class="col hide-on-small-only m3 l2">
                <ul class="section table-of-contents fixed">
                        <li><a href="#users">Users</a></li>
                        <li><a href="#actionstats">Action status</a></li>
                        <li><a href="#departments">Departments</a></li>
                        <li><a href="#workstreams">Workstreams</a></li>
                        <li><a href="#meetings">Meetitngs</a></li>
                        <li><a href="#kpis">KPIs</a></li>
                        <li><a href="#kpistat">KPI Statuses</a></li>

                </ul>
                </div>

## ACTIVATE ADD/EDIT BUTTONS ON SETUP PAGE
137. On setup page Create all the add item functionalities for Department, Workstream, Workstream, Meeting, KPI Status using steps as in a table below (more details can be found in the steps above) :

Step | Deparment | Workstream  | Meeting | KPI Status
----|------------| ------------| --------| -----------
step 1: Create Template in CLI                                                                  | ok | ok | ok | ok 
Step 2. Create link to template on setup page                                                   | ok | ok | ok | ok  
Step 3. Change basic template content                                                           | ok | ok | ok | ok
Step 4. Update form action parameter                                                            | ok | ok | ok | ok
Step 5. Input fields update (name, id, label for = MongDB key)                                  | ok | ok | ok | ok
Step 6. Create route decorator with methods parameter                                           | ok | ok | ok | ok
Step 7. Create basic py function to render template                                             | ok | ok | ok | ok
Step 8. inside function create method request if statement                                      | ok | ok | ok | ok
Step 9. inside if statement create new dictionary variable with request.form.get for inputs     | ok | ok | ok | ok
Step 10. inside if statement insert new variable inside mongo db                                | ok | ok | ok | ok
Step 11. add flash message and redirect to the page using url_for                               | ok | ok | ok | ok

138. Moved add next to each section heading title to make it consistent with user_dashboard page:

                <!--title and ad button popup-->
                <div class="row">
                    <div class="col s6">
                        <h5 class="align-left red-text text-darken-4"> <i class="fas fa-users"></i> USERS </h5>
                    </div>
                    <!--button "add_new"-->
                    <div class="col s4 right">
                        <h5> <a class="waves-effect waves-teal btn-flat" href="{{ url_for('add_user')}}"> ADD NEW </a></h5>
                    </div>
                </div>
                <hr><br>

139. Create Edit fiunctionality for all the buttons on setup page

Step                                                            | Deparment | Workstream  | Meeting | KPI  |  KPI Status |Action Status
----                                                            |-----------| ------------| --------| ----|  -- |--
step 1: Create Template in CLI                                  | ok | ok | ok |  ok | ok |no
step 2: setup Link to edit template                             | ok | ok | ok |  ok | ok |no
step 3: Update new edit template basic content                  | ok | ok | ok |  ok | ok |no
step 4: Update form action on edit template                     | ok | ok | ok |  ok | ok |no
step 5: Define route decorator to edit on app.py                | ok | ok | ok |  ok | ok |no
step 6: Create fnction for render template for edit on app.py   | ok | ok | ok |  ok | ok |no
step 7: update link with temlate ._id                           | ok | ok | ok |  ok | ok |no
step 8: include if statement in function request.method =="POST"   | ok | ok | ok |  ok | ok |no
step 9: add mongo db line int app.py function to insert new element| ok | ok | ok |  ok | ok |no
step 10: build input fields on edit template                       | ok | ok | ok |  ok | ok |no
step 11: connect value attribtes to edit object                    | ok | ok | ok |  ok | ok |no


## INPUT SHEETS TEMPLATE CREATE INPUT KPI FIELDS AND FUNCTIONALITY
140. on kpi_input page create input fields row above table heading (PROBLEM: The table inside the form did not work, so I used a css formatting that I used from stackoverflow - https://stackoverflow.com/questions/1893332/html-table-of-forms/9348667#9348667 ):

                <div class="table"> 
                <div class="table-row s12">
                        <div class="table-cell"> 
                        <input id="input_logdate" name="input_logdate" type="text" class="datepicker center-align" required>
                        <label for="input_logdate" >Log Date</label>
                        </div>
                        ....other input fields
                CSS formatting:
                .table { display: table; } 
                .table-row { display: table-row; }
                .table-cell { display: table-cell; }
        it is important to make sure that form is a parent tag of kpi inputs fields 
        
141. Develop kpi_input function route decorator and function to update kpi inputs into mongo db:

                # kpi inputs page - add input page
                @app.route("/kpi_input", methods=["POST","GET"])
                def kpi_input():
                # create kpi input variable for the select loop on kpi_input
                kpi = mongo.db.kpi.find()

                # if request method is post condition
                if request.method == "POST":
                        
                        # create a variable for kpi input
                        kpiinput={
                        "input_kpiname": request.form.get("input_kpiname"),
                        "input_logdate": request.form.get("input_logdate"),
                        "input_weeknumber": request.form.get("input_weeknumber"),
                        "input_uom": request.form.get("input_uom"),
                        "input_bsl": request.form.get("input_bsl"),
                        "input_tgt": request.form.get("input_tgt"),
                        "input_act": request.form.get("input_act"),
                        "input_status": request.form.get("input_status")
                        }
                        
                        # insert new kpi input inside kpiinputs collection
                        mongo.db.kpiinputs.insert_one(kpiinput)
                        
                        # show the message that the operation was done successfully
                        flash("KPI Input was successfully added")
                        
                        # redirect to home page
                        return redirect(url_for('home')) 
                return render_template("kpi_input.html", kpi=kpi)
142. Upload all the KPI inputs to KPI INput table
                
                a. download all the KPI inputs into the table:
                <!-- KPIS Summary - table body-->
                <tbody>
                        {%for input in kpiintputs %}
                        <tr>
                        <td>{{ input.input_logdate }}</td>
                        <td>{{ input.input_weeknumber }}</td>
                        <td>{{ input.input_uom }}</td>
                        <td>{{ input.input_bsl }}</td>
                        <td>{{ input.input_tgt }}</td>
                        <td>{{ input.input_act }}</td>
                        <td>{{ input.input_status }}</td>
                        </tr>
                        {%endfor%}
                </tbody> 
                b. update input_kpi function before if statement:
                # create kpiinouts variable for table body values
                kpiintputs=mongo.db.kpiinputs.find()
                c. update render_template part of the kpi_input function to includenew variable
                return render_template("kpi_input.html", kpi=kpi, kpiintputs=kpiintputs)

## CREATE FILTERING FUNCTIONALITY ON KPI INPUT PAGE
143. Add kpiowner filter to the KPI INput page:

                <div class="col s4">
                        <input value="{{user}}" id="input_kpiowner" name="input_kpiowner" type="text" class="validate"required>
                        <label for="input_kpiowner"></label>
                </div>
144. Update KPI input function with sesion user variable to pre-populate filter value in step 143:

                # define session user name
                user = session["user"]

                update input for the function:
                return render_template("kpi_input.html", kpi=kpi, kpiintputs=kpiintputs, user=user)

## CHANGE NAVBAR ACCESSIBILITY BASED ON MENTOR FEEDBACK 09-n0v
145. Copy Home link from 2 navbars and hide it behind login:

                <ul class="right hide-on-med-and-down">
                    <!--nav links always visible -->
                    {% if session.user %}  
                        {% if session.user|lower=="admin"|lower %}
                                <li><a href="{{ url_for('setup')}}">SET UP</a></li>
                        {% endif %} 
                    <li><a href="{{url_for('home')}}">MEETINGS</a></li>
                    <!--nav links visible when logged out-->
                        
                        <li><a href="{{url_for('user_dashboard', username=session['user'])}}">USER DASHBOARD</a></li>
                        <li><a href="{{url_for('kpi_input')}}">KPI INPUTs</a></li>
                        <li><a href="{{url_for('logout')}}">LOGOUT</a></li>
                        {% else %}
                            <li><a href="{{url_for('login')}}">LOGIN</a></li>
                            <li><a href="{{url_for('register')}}">REGISTER</a></li>
                    {% endif %}
                </ul>
## CEATE SEARCH FUNCTIONALITY ON INPUT PAGE

145. Go to python environment:

                CLI: python3
146. Import mongo from app (everything we have in our database is in this variable):
                
                CLI: from app import mongo
147. Create index for kpiinputs collection in mongodb:

                CLI: mongo.db.kpiinputs.create_index([("input_kpiname","text"),("input_kpiowner","text")]), 
                press ENTER
                We should have a following string: input_kpiname_text_input_kpiowner_text
148. Check MongoDb>mos>kpiinputs>indexes, we should see new index - input_kpiname_text_input_kpiowner_text
149. Check the details of the index created to confirm that index was created:

                CLI: mongo.db.kpiinputs.index_information()
                Result:
                {'_id_': {'v': 2, 'key': [('_id', 1)]}, 'input_kpiname_text_input_kpiowner_text': {'v': 2, 'key': [('_fts', 'text'), ('_ftsx', 1)], 'weights': SON([('input_kpiname', 1), ('input_kpiowner', 1)]), 'default_language': 'english', 'language_override': 'language', 'textIndexVersion': 3}}
150. Exit python environment on CLI:

                CLI: quit()
151. Create filter function on app.py:

                # filter function for kpi inputs page
                @app.route("/filter", methods = ["GET" , "POST"])
                def filter():
                        #  enable kpii for loop after filtering  
                        kpi = mongo.db.kpi.find()
                        
                        # make second from work after the filtering
                        input_kpiname = request.form.get("input_kpiname")
                        
                        # create variable for automatic KPI definition on the kpi input line 
                        kpiselection = input_kpiname
                        
                        # create inputs variable for KPI inputs list based on search request
                        kpiintputs = list(mongo.db.kpiinputs.find({"$text": {"$search":input_kpiname}}))
                        
                        # create inputs variable for KPI inputs list based on search request
                        return render_template("kpi_input.html", kpiintputs=kpiintputs, 
                                kpi=kpi, kpiselection=kpiselection)
152. launch filter function with button:

                <!--KPI Inputs-->
                <div class="row card-panel grey lighten-5 s12">
                        <!--form for filter button-->
                        <form action="{{url_for('filter')}}" method="POST" class="s12">
                                <!--Filters Section-->
                                <div class="row">
                                        <!--Filter dropdown-->
                                        <div class="col s6">
                                        <select id="input_kpiname" name="input_kpiname" class="materialize-textarea validate" required>
                                                <option value="" disabled selected>{{ kpiselection }}</option>
                                                {%for kp in kpi%}
                                                <option value="{{kp.kpi_name}}">{{kp.kpi_name}}</option>
                                                {% endfor %}
                                                <label for="input_kpiname"></label>
                                        </select>
                                        </div>
                                        <div class="col s2 center-align">
                                        <button type="submit" class="waves-effect blue-grey btn">
                                                <i class="fas fa-sort-amount-down"></i>
                                        </button>
                                        </div>
                                        <!--Reset button-->
                                        <div class="col s left">
                                        <a href="{{url_for('kpi_input')}}" class="red btn text-shadow"><i class="fas fa-refresh"></i></a>
                                        </div>
                                </div>
                        </form>

## KPIINPUTS: ADD EDIT FUNCTIONALITY TO EACH ROW ON KPI INPUTS TABLE

153. Add Edit template based on edit_kpi

                CLI: cp template/edit_action.html templates/edit_kpiinput.html

154. Create inputs on edit-kpiinput template:
                
                <!-- kpiinputs -->
                <!-- kpiinput name - text-->
                <div class="row">
                    <div class="input-field col s12">
                        <input value="{{input.input_kpiname}}" id="input_kpiname" name="input_kpiname" type="text" class="validate" required>
                        <label for="input_kpiname">KPI name</label>
                    </div>
                </div>
                <!-- kpiinput logdate - datepicker -->
                <div class="row">
                    <div class="input-field col s12">
                        <i class="fas fa-calendar-alt prefix"></i>
                        <input value="{{input.input_logdate}}"id="input_logdate" name="input_logdate" type="text" class="datepicker validate" required>
                        <label for="input_logdate" >Log Date</label>
                    </div>
                </div>
                <!-- kpiinput weeknumber - text-->
                <div class="row">
                    <div class="input-field col s12">
                        <input value="{{input.input_weeknumber}}" id="input_weeknumber" name="input_weeknumber" type="text" class="validate" required>
                        <label for="input_weeknumber">Weeknumber</label>
                    </div>
                </div>
                <!-- kpiinput uom - text-->
                <div class="row">
                    <div class="input-field col s12">
                        <input value="{{input.input_uom}}" id="input_uom" name="input_uom" type="text" class="validate" required>
                        <label for="input_uom">Unit of measure</label>
                    </div>
                </div>
                <!-- kpiinput bsl- text -->
                <div class="row">
                    <div class="input-field col s12">
                        <input value="{{input.input_bsl}}" id="input_bsl" name="input_bsl" type="text" class="validate" required>
                        <label for="input_bsl">Baseline</label>
                    </div>
                </div>
                <!-- kpiinput tgt- text -->
                <div class="row">
                    <div class="input-field col s12">
                        <input value="{{input.input_tgt}}" id="input_tgt" name="input_tgt" type="text" class="validate" required>
                        <label for="input_tgt">Target</label>
                    </div>
                </div>
                <!-- kpiinput act- text -->
                <div class="row">
                    <div class="input-field col s12">
                        <input value="{{input.input_act}}" id="input_act" name="input_act" type="text" class="validate" required>
                        <label for="input_act">Actual</label>
                    </div>
                </div>
                <!-- kpiinput status - text -->
                <div class="row">
                    <div class="input-field col s12">
                        <input value="{{input.input_status}}" id="input_status" name="input_status" type="text" class="validate" required>
                        <label for="input_status"> Status </label>
                    </div>
                </div>
                <!-- kpiinput owner - select -->
                <div class="row">
                    <div class="input-field col s12">
                        <select id="input_kpiowner" name="input_kpiowner" class="materialize-textarea validate" required>
                            <option value="{{input.input_kpiowner}}" disabled selected>{{user}}</option>
                            {%for owner in owners %}
                                <option value="{{owner.user_name}}">{{owner.user_name}}</option>
                            {%endfor%}
                        </select>
                        <label for="input_kpiowner">KPI Owner</label>
                    </div>
                </div>
155. Create app.py function

                # create edit_kpi input function
                @app.route("/edit_kpiinput/<kpiinput_id>", methods=["POST", "GET"])
                def edit_kpiinput(kpiinput_id):
                
                        # create kpiinput variable to prefill kpiinput input values in the form
                        input = mongo.db.kpiinputs.find_one({"_id": ObjectId(kpiinput_id)})

                        # variable for kpiowners select
                        owners = mongo.db.users.find()

                        # variable for KPIs list select
                        kpis = mongo.db.kpi.find()

                        # user variable
                        user = session["user"]

                        # update changed kpiinput data into mongodb
                        if request.method == "POST":
                                editkpiinput = {
                                        "input_kpiname": request.form.get("input_kpiname"),
                                        "input_logdate": request.form.get("input_logdate"),
                                        "input_weeknumber": request.form.get("input_weeknumber"),
                                        "input_uom": request.form.get("input_uom"),
                                        "input_bsl": request.form.get("input_bsl"),
                                        "input_tgt": request.form.get("input_tgt"),
                                        "input_act": request.form.get("input_act"),
                                        "input_kpiowner": user,
                                        "input_status": request.form.get("input_status")
                                }
                                
                                # insert new kpiinput into Mongo Db database
                                mongo.db.kpiinputs.update({"_id": ObjectId(kpiinput_id)}, editkpiinput)

                                flash("KPI input update successfull!")
                                
                                return redirect(url_for('kpi_input'))
                        return render_template("edit_kpiinput.html",  input=input, 
                                user=user, owners=owners, kpis=kpis)
156. Link kpi_input to edit_kpiinput template:

                <!-- KPIS Summary - table body-->
                <tbody>
                        {%for input in kpiintputs %}
                        <tr>
                                <td>{{ input.input_kpiname }}</td>
                                <td>{{ input.input_logdate }}</td>
                                <td>{{ input.input_weeknumber }}</td>
                                <td>{{ input.input_uom }}</td>
                                <td>{{ input.input_bsl }}</td>
                                <td>{{ input.input_tgt }}</td>
                                <td>{{ input.input_act }}</td>
                                <td>{{ input.input_status }}</td>
                                <td><a href="{{ url_for('edit_kpiinput',  kpiinput_id = input._id)}}" class="btn blue-grey">EDIT</a>
                                </td>
                        </tr>
                        {%endfor%}
                </tbody> 

157. Hide buttons for non admin users - still to do.

## USER_DASHBOARD: DEVELOP AND IMPLEMENT FUNCTIONALITY OF UPDATING A KPI LIST
158. on add_kpi function in app.py add additional zero field that are generated automaticaly but not visible to the admin

                # setp admin kpi inputs page
                @app.route("/add_kpi", methods=["POST","GET"])
                def add_kpi():
                # add select dropdown list
                owners = mongo.db.users.find()

                # add kpi into mongodb
                if request.method=="POST":
                        kpi={
                        "kpi_name": request.form.get("kpi_name"),
                        "kpi_shortname": request.form.get("kpi_shortname"),
                        "kpi_uom": request.form.get("kpi_uom"),
                        "kpi_owner": request.form.get("kpi_owner").lower(),
                        "kpi_description": request.form.get("kpi_description"),
                        "kpi_lastlstatus": "grey"
                        }
                        # insert new document into mongodb collection kpi
                        mongo.db.kpi.insert(kpi)
                        # print completion on th escreen
                        flash("KPI was successfully added!")
                        # redirect to setup
                        return redirect(url_for('setup'))
                return render_template("add_kpi.html", owners=owners)

159. on add_kpiinput when new input is added logdate is compared to the one stored in kpi collection, if it is higher it updates the values (logdate, bsl, tgt, act, status) in kpi collection with new ones. (inside if reguest.method==['POST']):

                # based on kpiinput define a variable to update  kpi collection fields
                latestinput ={
                "kpi_lastlogdate": request.form.get("input_logdate"),
                "kpi_lastbsl": request.form.get("input_bsl"),
                "kpi_lasttgt": request.form.get("input_tgt"),
                "kpi_lastact": request.form.get("input_act"),
                "kpi_laststatus": request.form.get("input_status")
                }
                
                # update kpi collection for specific fields following MongoDb documentation -https://docs.mongodb.com/manual/reference/operator/update/set/. 
                mongo.db.kpi.update({"kpi_name": request.form.get("input_kpiname")},{"$set":latestinput})
        I encountered a problem here -  the code {$set:latestinput} did not work Johann from student support helped me - i corrected the code and added "" - {"$set":latestinput}. 
                

160. on edit_kpiinput when new input is edited logdate is compared to the one stored in kpi collection, if it is higher it updates the values (logdate, bsl, tgt, act, status) in kpi collection with new ones

                # based on kpiinput define a variable to update  kpi collection fields
                latestinput ={
                "kpi_lastlogdate": request.form.get("input_logdate"),
                "kpi_lastbsl": request.form.get("input_bsl"),
                "kpi_lasttgt": request.form.get("input_tgt"),
                "kpi_lastact": request.form.get("input_act"),
                "kpi_laststatus": request.form.get("input_status")
                }
        
        # update kpi collection:
        mongo.db.kpi.update({"kpi_name": request.form.get("input_kpiname")},{"$set":latestinput})

161. on userdashboard template kpi status is updated using for loop

                step1: inside user_dashboard function on app.py add kpis variable:
                # create kpis variable for for loop for kpis
                kpis=mongo.db.kpi.find()
                
                step 2: on user_dashboard tmplate create for loop to update table:
                <!-- KPIS Summary - table body-->
                <tbody>
                        {% for kpi in kpis %}
                        <tr>
                        <td>{{kpi.kpi_name}}</td>
                        <td>{{kpi.kpi_uom}}</td>
                        <td>{{kpi.kpi_lastbsl}}</td>
                        <td>{{kpi.kpi_lasttgt}}</td>
                        <td>{{kpi.kpi_lastact}}</td>
                        <td>
                                {%if kpi.kpi_laststatus=="red" %}
                                <h5><i class="fas fa-times-circle red-text"></i></h5>
                                {%elif kpi.kpi_laststatus=="green"%}
                                <h5><i class="fas fa-check-circle green-text"></i></h5>
                                {% else %}
                                <h5><i class="fas fa-circle grey-text"></i></h5>
                                {%endif%}
                        </td>
                        <td class="s12 m3">
                                <a href="{{url_for('add_action')}}" class="btn blue-grey text-shadow">ACTION</a>
                        </td>
                        </tr>
                        {% endfor%}

162. on userdashboard use search functionality to filter the list of kpis depending on user

                step1: create search index for kpi collection in python3
                CLI: from app import mongo
                CLI: mongo.db.kpi.create_index([("kpi_owner","text")]) => 'kpi_owner_text'

                step2: create ufnctionality to filter users based on kpi owner, admin should see all the kpis:
                # define variable for automatic filter
                user=session["user"]
                
                step 3: define if conditions and use index filtering functionality inside user_dashboard function:
                # define variables for kpis and actions loop -it should be filtered to user as kpi_owner, and if it is admin it should not filter, this nested conditions should also be used for filter section of actions
                if user == "admin":
                        
                        # variable kpis for KPIs section when user is logged in as admin
                        kpis = mongo.db.kpi.find()
                        
                        # variable kpis for KPIs section when user is logged in as admin
                        actions = mongo.db.actions.find() 
                        
                        # action status filtering condition - activated after the action status is selected
                        if request.method == "POST":
                        actions = list(mongo.db.actions.find({"action_status":action_status}))
                
                # this part of the function is activated when the user logged in as non-admin
                else:
                        # create kpis for KPI summary section if the user is non-admin
                        kpis = list(mongo.db.kpi.find({"$text":{"$search":user}}))
                        # create actions variable for non-admin
                        actions = list(mongo.db.actions.find({"action_accountable": user}))
                        # create actions variable for non-admin when filter is activated
                        if request.method == "POST":
                        # this filter has 2 filters - user and action status that is selected from filter section
                        actions = list(mongo.db.actions.find({"action_accountable": user, "action_status":action_status}))   
                

163. on user dashboard kpi summary table - Add different buttons depending on kpi status red - action button, grey - kpi inputs button:
                
                {%if kpi.kpi_laststatus=="red" %}
                        <td>
                            <i class="fas fa-times-circle red-text"></i>
                        <td class="s12 m3">
                            <div class="col s3">
                                <a class="red btn text-shadow" href="{{ url_for('add_action')}}"> ACTION </a>
                            </div>
                        </td>
                        {%elif kpi.kpi_laststatus=="green"%}
                            <td>
                                <i class="fas fa-check-circle green-text"></i>
                            </td>
                            <td>  </td>
                        {% else %}
                            <td>
                                <i class="fas fa-circle grey-text"></i>
                            </td>
                            <td class="s12 m3">
                                <a href="{{url_for('kpi_input')}}" class="btn blue-grey text-shadow"> INPUT </a>
                            </td>                    
                    {%endif%}
                </tr>
164. Correct responsiveness of the KPI summary table:

                <!--Card panel for KPI summary table-->
                <div class="card-panel">
                        <table class="responsive-table highlight centered">
                
                
## FIX ACTIONS TABLE ON USER_DASBOARD TEMPLATE 
165. Replace existing collapsible with table and for loop

                <!-- Actions table -->
                <div class="card-panel">
                        <table class="responsive-table highlight centered">
                        <!-- Actions table - headings-->
                        <thead>
                                <tr class="grey lighten-2">
                                <th>No.</th>
                                <th>Action</th>
                                <th>Accountable</th>
                                <th>Deadline</th>                                        
                                <th>Status</th>                                        
                                <th>  </th>                                        
                                <th>Edit</th>                                        
                                </tr>
                        </thead>
                        <!-- KPIS Summary - table body-->
                                ...
166. on user_dashboard add actioon loop :

                <!-- KPIS Summary - table body-->
                <tbody>
                        {% for action in actions %}
                        <tr>
                        <td>{{action.action_refno}}</td>
                        <td>{{action.action_name}}</td>
                        <td>{{action.action_accountable}}</td>
                        <td>{{action.action_due}}</td>
                        <td>{{action.action_status}}</td>
167. on user_dashboard Add status status check to assign the icon for each status:

                <td>{{action.action_status}}</td>
                {%if action.action_status=="not done" %}
                        <td>
                            <i class="fas fa-times-circle red-text"></i>
                        </td>
                        {%elif action.action_status=="done"%}
                            <td>
                                <i class="fas fa-check-circle green-text"></i>
                            </td>
                        {%elif action.action_status=="paused"%}
                            <td>
                                <i class="fas fa-pause-circle yellow-text"></i>
                            </td>
                        {% else %}
                            <td>
                                <i class="fas fa-circle grey-text"></i>
                            </td>               
                {%endif%} 

168. on user_dashboard use if statement to define 2 buttons 1 for admin user and 1 for all the other users:

                <!--add full edit right button for admin and statusedit right button for other users-->
                {% if user == "admin" %}
                        <td><a href="#" class="btn blue-grey">EDIT</a></td>
                {% else %}
                        <td><a href="#" class="btn blue-grey">CHANGE STATUS</a></td>
                {% endif %}

169. Add filter buttons to filter actions on user_dashboard:

                <form action="#" method="POST" class="s12">
                <!--Filters Section-->
                <div class="row">
                        <!--Filter dropdown-->
                        <div class="col s6 m4">
                        <select id="completionstatus_name" name="completionstatus_name" class="materialize-textarea validate" required>
                                <option value="" disabled selected>{{ kpiselection }}</option>
                                {%for cs in completionstatus%}
                                <option value="{{cs.completionstatus_name}}">{{cs.completionstatus_name}}</option>
                                {% endfor %}
                                <label for="completionstatus_name"></label>
                        </select>
                        </div>
                        <div class="col s2 center-align">
                        <button type="submit" class="waves-effect blue-grey btn">
                                <i class="fas fa-sort-amount-down"></i>
                        </button>
                        </div>
                        <!--Reset button-->
                        <div class="col s left">
                        <a href="{{url_for('user_dashboard',username=session["user"])}}" class="red btn text-shadow"><i class="fas fa-refresh"></i></a>
                        </div>
                </div>
                </form>
170. Fix add_action template - add status field and update py function

                add_achtion change 
                <!--9. Current status - select-->
                <div class="row">
                    <div class="input-field col s12">
                        <i class="fas fa-medal prefix"></i>
                        <select id="action_status" name="action_status" class="validate" required>
                            <option value="" disabled selected></option>
                            {%for status in completionstatus%}
                                <option value="{{status.completionstatus_name}}">{{status.completionstatus_name }}</option>
                            {%endfor%}
                        </select>
                        <label for="action_status">Completion Status</label>
                    </div>
                </div>
                update app.py:
                if request.method=="POST":
                        # create a variable for new action
                        task={
                        "action_refno": request.form.get("action_refno"),
                        "action_name": request.form.get("action_name"),
                        "action_due": request.form.get("action_due"),
                        "action_accountable": request.form.get("action_accountable"),
                        "action_dept": request.form.get("action_dept"),
                        "action_logdate": request.form.get("action_logdate"),
                        "action_meeting": request.form.get("action_meeting"),
                        "action_workstream": request.form.get("action_workstream"),
                        "action_status": request.form.get("action_status")
                        }
                        
                        # insert new action inside actions collection
                        mongo.db.actions.insert_one(task)
                        
                        # show the message that the operation was done successfully
                        flash("New action was successfully added")
                        return redirect(url_for('user_dashboard', username=session['user']))


169. Create edit_action for admin and edit_actionstatus for non-admiin templates and py function for it:
        
STEPS | Functionality | code |edit action | edit action status
--|--|--|--|--
step1: CLI copy | cp templates/edit_kpistatus.html | na |ok | ok
step2: Content | html  |edit_actionstatus.html,edit_action.html,  |ok | ok
step3: link and form on user_dashboard page | html user_dashboard.html | lines  |ok | ok
step4: Connect by funtion in py | app.py row| 663,689  |ok | ok

## ADD SPYSCROLL ON USER DASHBOARD
170. Add 

## OTHER PROBLEMS TO SOLVE
still to do:
- fix user_dashboard link
- populate user-dashboard kpi summary based on user who logged in, find a way how to connect lastkpi inputs to user_dashboard
- link mongo DB to Power Bi 
- link Power BI to an app on a home page
- crete defensive code by making an if statuement on each page after login (recommendation by mentor 09-nov)
- fix responsiveness issue on a kpiinouts page
- fix edit kpiinput submit button issue - it works only if i usedropdown list


