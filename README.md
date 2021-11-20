# MS3 - Management Operating System (MOS) - Meetings Hub
![am_i_responsive](static/img/amiresponsive.jpg)
#

## **Introduction**

  A "M-Hub" - Meeting Hub project is a web application to digitalise an effective performance management via structured meetings focused on Key Performance Indicators (KPIs) and corrective actions. The app is built based on one of the modules of "Digital Results Hub"(DRH) - a solution developed for a real consulting company. This module helps to digitise  Management Operatiing System (MOS) elements of the consulting methodology. 
  "Meeitngs Hub" is a part of more extensive solution that was developed in 2021 by a global consulting company. Initial solution consists of 4 modules and "Meetings Hub" is one of 4 modules.
  "Meeitngs Hub" consists of meetings, KPIs adn actions reviewed during the meetings. Meeting Hub solution is a digital product that is normally installed at the client's site. It helps the client to improve meetings quality and manage productivity through standard process of looking at performance trends and defiining actions to address the variance between plananed and actual performance. 
  hwen started the application was built for educational purposes only.

Link to the Application: [Meetings Hub](http://ask-pft-meetinghub.herokuapp.com/)
Step-By-Step development process is [here](sbsdev.jpg):
#
## **User Experience (UX)**
### **GOALS**
There are 4 goals of this appliaction:
1. **For developer** - as a codeinstitute student I wanted to create an appliation as close to a real solution as possible- an  application close to real product that is currently in demand. It would help me to demosntrate the developer skills for potential employer in consulting industry. With further improvement it can potentially be sold to my employer who currently develops Digital Results Hub using other platforms (Javascript, Azure, Power Bi, Sharepoint etc.)
2. **For client** - the application will help a meeting chair to navigate thorugh KPIs Viusuals during the meeting, by using filters KPIs will be filtered by accountability. The performance of each participant will be visualised through Key Perrformance Indicators and those KPIs that require action effort will be conditionally highlighted. The visualisation will help to quickly identify the preformance level and address the variance with actions assigned to meeting participants.
3. **For user with admin right** - the application will help the user with admin rihgths to administer inputs for KPIs, inputs for actions, update actions statuses. That will be done prior to the meetings defined in applications
4. **For all the other users** - it will help to get an access to up to dat information about kpi data and actions, helping them to report about department effectiveness and performance throguh result oriented actions during the meeting. 
#
### **USER STORIES**
#### As a Developer
  - _USER STORY 1_: Developer can use an app to show how the software development skils can add value to consulting skills. 

#### As an admin Site User
  - _USER STORY 2_: The admin user registers with super admin rights
  - _USER STORY 3_: The admin user defines a system elements parameters: roles,  participants, participants rights, meetings structure, meetings inputs parameters (KPIs and Actions), define accountability for teh KPIs and Atcions, edit actions and kpiinputs, define link to meeting dashboards
  - _USER STORY 4_: The admin user prepares for the meeting prior to the meeting: edit/add KPIs inputs, update actions, 
  - _USER STORY 5_: The admin user enters new actions after each meeting based on results of the meeting
  - _USER STORY 6_ : search actions by completion status, search kpi data inputs
  - _USER STORY 7_ : navigate through the navigation
  - _USER STORY 8_ : use mobile phone to execute the same functions as PC version

#### As a regular User
  - _USER STORY 9_ : Check the status of curent actions, check if new actions are needed, update the status of existing actions
  - _USER STORY 10_ : add new kpi data inputs from blank form, add new kpis by copying them from existing kpis 
  - _USER STORY 11_ : search actions by completion status, search kpi inputs by various parameters (name, week, status, owner)
  - _USER STORY 12_: intuitively navigate through the pages (navbar  and buttons)
#
### **DESIGN PROCESS**
In UX design process I used 5 planes according to Jesse James Garret who wrote an article on 5 planes of UX design, more information can be found [here](https://mersus.io/user-experience-design-corporate-vr/) - Strategy Plain, Scope Plain, Structure Plain, Skeleton PLain, Surfce Plain:
* _Strategy Plain_: 
The strategy plain is best explained throguh the client's needs, so early in the process I have defined basic client needs that client wants to meet with my application:
  * _CLEINT NEEDS_
    * The application is a product for the client. The client has a need to digitise meetings and standardise the way they are conducted to make them maximum effective. 
    * Therefore, the Client as achair needs to have a meeting dashboard to review the KPIs (Key Performance Indicators), while reviewing KPIs s/he also needs to see which indicators actual performance is behind the target, assign actions for those that are behind and follow up on actions completion next meeting. 
    * That means that each participant will have a KPIs assigned to him. In order to be effective during the meeting s/he will need to prepare prior to the meeitng by 
      1) updating the baseline, target and actual for each KPI that s/he is accountable for - that will be called "kpi input" for each meeting occasion, 
      2) creating a new action If the KPI has a red status  
      3) checking that actions assigned to her(him) are done, and therefore updating the status appropriately
    * In order to be functional there must be a special user who will administer the application. This user will have a special admin rights. Admin right will allow this user to:
      1) Assign the right to any other user
      2) Set basic parameters for major inputs such as user name, kpi, actions, meetings, departments, action completion status and kpi input status. 
      3) This user with special rights will need an access to all the actions and kpi inputs that other user input 
      4) in order to navigate through setup, action and kpi parameters admin user will need to have a search options provided to him
    * The aplication needs to have a front-end interface, that means it needs to be web-based
    * Since we will have various kpi and action data points we need to use an external data storage and hence implement CRUD functionality between forntend and the database
    * it is also important that the application has restricted access with login and password and basic security features
    
* _Scope Plain_: 
 Based on the client needs outlined in previous section we will need define features that will be implemented in the application based on 3 types of rights - developer, admin and user rights
    * The table below defines the scope, user rights and access to various application components:

      No. | Category                                | Developer  | Admin rights | User rights
      ----|---------                                | ------| ----| -----
      01  | Register                                | Yes   |Yes  | Yes 
      02  | Login                                   | Yes   |Yes  | Yes 
      03  | Set up users rights                     | Yes   | No*  | No
      04  | Set up roles                            |  Yes  | Yes  | No 
      05  | Set up users                            |   Yes | Yes | No 
      06  | Set up meetings                         |   Yes | Yes | No   
      07  | Set up meeting content                  |   Yes | no  | No   
      08  | Set up KPIs                             |   Yes | Yes | No  
      09  | Edit Actions                            |   Yes | Yes | No  
      09  | Edit Action status and add new actions  |   Yes | Yes | Yes  
      10  | Design Visual Dashboard in BI platform  |   Yes | No  | No     
      10  | Define inputs for visual dashboard      |   Yes | No  | No     
      11  | Filter Visual Dashboard parameters      |   Yes | Yes | no  
      12  | Copy/Add KPI inputs                     |   Yes | Yes | No   
      13  | Edit KPI inputs at any tiime            |   Yes | Yes  | No  
      14  | Update Actions completion status        |   Yes | Yes | No 
      16  | Archive Meeting dashboard as pdf        | Yes   | Yes | No

  
  * The table below defines what pages need to be developed within ms3 assignment requirement
      Feature                      | in scope 
    ---------                     |--------- 
    User registration | in scope 
    Cleint login |    in scope 
    Admin access with wider access | in scope 
    intuitive navigation |in scope 
    Individual dashboard with user KPI summary |   in scope  
    individual dashboard with user actions  |   in scope  
    KPI Input add / edit/ copy  |   in scope 
    Actions add/edit |  in scope 
    Actions status updates | in scope 
    Database storage in cloud-based non-relational database - MongoDB | in scope
    CRUD Functionality for Actions |in scope 
    CRUD Functionality for KPI inputs | in scope 
    CRUD Functionality for setup parameters (user, kpi action etc.) | in scope  
    Admin rights defined through front end | in scope 
    Meeting dashboard - filter for each meeting |  in scope 
    Meeting dashboard visualisation |  NOT IN SCOPE 
    Dashboard design | NOT IN SCOPE 
    Connect Power BI to the MongoDB Database | NOT IN SCOPE 
    Connecting to the client Database | NOT IN SCOPE 
    Sending email to the user prior to the meeting | NOT IN SCOPE 

* _Structure Plain_:
Once we understnd what the needs and the structure within appliaction scope is, we built 3 documents to show application flow, technology, data structure and database schema, it also cover all the features that will be built into the application:
  * Link to [Structure](static/img/structure.jpg) - the structure was built in MS PowerPoint
  * Link to [Workflow and tools](/static/img/workflow_tools.jpg) - the flow was built in MS PowerPoint.
  * Link to [Schema](static/img/schema.jpg) - the schema was built in PowerPoint.
Features list 


* _Skeleton Plain_:
After that we developed wireframes that help us undertsand how the application should look like on PC and mobile phone:
  * [Link to responsive Wireframe file in pdf](https://drive.google.com/file/d/1fsWrmySpizFI2vYiG_p664LLvPUs-nNF/view?usp=sharing)
![wireframe](static/img/wireframe.jpg)


* _Surface Plain_:
Website colors and design should be simple, neutral and functional, it means - limited amount of colors. Colors focused only in higlights. Icons should serve the functionality. ANd help the user to intuitively navigate the site. below we summarised icons, colors and 
  * **Colour Pallette** _Source_: [Materialise](https://materializecss.com/)

    Element | Color Materialise classes| Code
    -|-|-
    Pages Backgorund | white |rgba(0,0,0,0.87)
    Text color - Active|grey darken-4 | #212121  
    Text color - Titles|red darken-4 | #b71c1c
    Text color - other text|grey lighten-1|#bdbdbd 
    Navbar background|blue-grey lighten-5| #eceff1 
    Mobile sidebar backgroud|blue-grey lighten-3|#b0bec5 
    Visuals - KPI actuals|blue-grey lighten-1|#78909c
    Visuals - KPI baseline|brown lighten-3| #bcaaa4 
    Visuals - KPI target|blue-grey darken-4| #263238 
    Visuals - action status - complete| green accent-4|#00c853
    Visuals - action status - not complete|red| #f44336 
    Non-contracts Icons|blue-grey lighten-4| #cfd8dc
    Contrast Icons|blue-grey darken-1|#546e7a

  * **Fonts**
  I tested 2 types of font combitation limiting the choice to 2 traditional business fonts pairs:
    - "Roboto" and "Sans Serif", 
    - "Lato" and "PT Sans".
  
  * **Icons**
    
    Icons form FontAwesome were chosen randomly and summarised in the table below:
    Template  | icon | FontAwesome code
    -|-|-
    register | name                       | fas fas fa-user-plus
    register | email                      | fas fa-envelope
    register |  password                  | fas fa-unlock
    register |  button                    | fas fa-running, fas fa-sign-in-alt
    login |  name                         | fas fa-user-cog
    login |  password                     | fas fa-user-lock
    login |  button                       | fas fa-sign-in-alt
    user_dashboard |  Actions             | fas fa-list
    user_dashboard |  filter button       | fa-sort-amount-down
    user_dashboard |  filter refresh button       | fas fa-refresh
    user_dashboard |  action status not done  | fa-times-circle
    user_dashboard |  action status done  | fas fa-check-circle
    user_dashboard |  button status paused  | fas fa-pause-circle
    user_dashboard |  button status not started  | far fa-circle
    user_dashboard |  KPI Summary         | fas fa-chart-line
    kpi_input |  KPI Inputs               | fas fa-chart-line, fas fa-caret-right
    kpi_input |  filter               | fas fa-sort-amount-down
    kpi_input |  filter               | fas fa-refresh
    add_action | Action number        | fas fa-list-ol
    add_action | Logdate              | fas fa-calendar-alt
    add_action | Action  name         | fas fa-ellipsis-h
    add_action | Due Date             | fas fa-calendar-check
    add_action | Accountable          | fas fa-user
    add_action | Department           | fas fa-building
    add_action | Meeting              | fas fa-users-cog
    add_action | Worksream            | fas fa-stream
    add_action | Completion Status    | fas fa-medal
    edit_kpiinput | KPI name    | fas fa-ellipsis-h
    edit_kpiinput | KPI logdate    | fas fa-calendar-alt
    edit_kpiinput | Weeknumber    | fas fa-calendar-week
    edit_kpiinput | Unit of Measure    | fas fa-ruler
    edit_kpiinput | baseline    | fas fa-terminal
    edit_kpiinput | target    | fas fa-crosshairs
    edit_kpiinput | Actual    | fas fa-chart-bar
    edit_kpiinput | Status    | fas fa-medal
    edit_kpiinput | Owner    | fas fa-user

#
### **FEATURES**
### **Features implemented**
  no. | Feature | Page | Status 
  --  |--       |--     |--
  1   | Template using Flask                                  | base.html                                               | done
  2  | Register page with basic security requirements         | register.html                                           | done
  3  | Login page  for other users                            | login.html                                              | done
  4  | Navbar on base template + mobile navbar                | base.html                                               | done
  5  | Input forms                                            | add_action, kpi_inputs + 6 templates connected to setup | done
  6  | Edit input forms                                       | 9 templates - edit_kpi                                  | done
  7  | Show buttons based on user rights                      | user_dashboard                                          | done
  8  | Connect input forms to MongoDb                         | app.py                                                  | done
  9  | Dropdowns based on materialise select library          | add/edit templates, app.py, js                          | done
  10 | Calendar datepicker                                    | add/edit templates, app.py                              | done
  11 | Calendar datepicker                                    | add/edit templates, app.py                              | done
  12 | For loops to visualise content form mongo collections  | user_dashboard, app.py                                  | done
  13 | Automatic filtering inside for loops based on user login | user_dashboard, app.py                                | done
  14 | Dropdown filters of actions and KpIs for "for" loops   | user_dashboard, kpiinput, app.py                        | done
  15 | Automatic icons setup based on action status           | user_dashboard, app.py                                  | done 
  16 | Table buttons that depend on user on KPI status        | user_dashboard, app.py                                  | done 
  17 | Cancell buttons to return to user_dashboard            | add/edit forms                                          | done 
  18 | CREATE new inputs as mongo document in collection      | user_dashboard, kpi_inputs, app.py                      | done  
  19 | READ inputs in mongodb document in collection          | user_dashboard, kpi_inputs, app.py                      | done 
  20 | UPDATE inputs in mongodb document in collection        | 9 edit forms, app.py                                    | done 
  21 | DELETE inputs / documents in collection                | setup, app.py                                           | done 
  22 | Spyscroll for long pages                               | setup, app.py, js, materialise                          | done 

How the features look like:
![Features](static/img/features.jpg)

### **Features Not implemented:**
1. Connecting MongoDb to power BI using ODBC connector. 
2. Add button to send Email to each user once actions and kpis are updated by admin before to the meeting
3. Generate pdf report for each user latest KPIs status and actions that are due and not done
4. Add actions list that is related to the meeting on meeting dashboard with functionality to sort them by user
5. Admin rights are connected to the role defined by admin user - I know how to do it, but runnint short of time.

### **TECHNOLOGIES**
  * **Languages**
    - _HTML_ - Hyperlinked markup language, to develop 
    - _CSS_ - cascading style sheets to decorate html webpages, I used basic decoration with litle attention to design, focusing on functionality
    - _Javascript_ - programming language for interactive experienc, in this project I used it only for certain front-end features.
    - _Python_ - programming language to 
  * **Libraries**
    - _Flask_ - python library to use templates and integrate backend data (stored on MongoDb) with forntend application, falsk helps to reduce amount of html development and use  python with html.
    - _Materialize_ - css library with common wed elements - used to save time on developing buttons, navbars, sidebars, and website responsiveness
    - _FontAwesome_ - icons collection - used for UX design.
    - _JQuery_ - simplified JavaScript library - to reduce amount of js coding.
  * **Tools**
    - _Mongo DB_ - non-relational cloud based database storage
    - _Power Bi_ - Business Intelligence visualisation tool, the access was rovided by current employer Alexander Proudfoot consulting
    - _GitPod_ - clud based edi pogramming environment
    - _GitHub_ - cloud based development repository - this project is saved on askfrsltn profile.
    - _CLI_ - command line interface used to 
    - _Heroku_- it is clud based platform to build, and run web applications, in this project used to deploy the application to the web  
    - _MS Powerpoint_- was used to build visual structure, flow, data schema, and wireframes.  
    - _GoogleDrive_- used to store the wireframe document in pdf format.

#
## **[TESTING](/testing.md)**
Testing consist of (1) UserStories testing, (2) Navigation testing, (3) Accessibility testing, (4) Responsiveness testing, (5) Browser compatibility testing (5) Code Validation, (6) Site Performance testing. Testing is descibed on another file [here](/testing.md)
  #### **UserStories testing** - In this section each user story (see section "User Experience") is tested through appliaction functionality - see the result [here]()
  #### **Navigation** -  In this section I test the navigation through the application - functionality of the buttons, links, inputs, conection to MongoDb - see the result [here]()
  #### **Accessibility testing** -  In this section I describe how basic security was tested - I tried to access different pages/temmplates - see the result [here]()
  #### **Responsiveness testing** -  In this section - see the result [here]()
  #### **Browser Compatibilty** -  In this section - see the result [here]()
  #### **Code Validation** -  In this section HTML, CSS, JavaScript, Python -see the result [here]()
  #### **Site Perromance Testing** -  In this section I use Lighthoouse by Google Chrome to test Site Performance - see the result [here]()

#
## DEPLOYMENT
Theree are 4 sections in this chapter - (1) hosting on GitHub, Forking GitHUb repo, (2) Forking the repository (3) Running the project Locally and (3)Deploying th eapplication to Heroku.
Working with Github and using Git was needed to host and develop the code in the cloud while Heroku was used to deploy the application to the web.  

### GITHUB
### **(1) Open a new repo:**
  - Register into own account on GitHub
  - Press gree Button "new"
  - On repository template select Code-institute-Org/gitpod-full-template
  - Next to the "Owner" type "Repository Name"
  - Select "public" option
  - Press green button "Create Repository" = ? new repository created based on standard Code Institute template
  - Press green button "Gitpod" - you will be prompted to cloud based EDI wher you can start editing the application code and README file.

### **(2) Forking the GitHub Repository**
To fork a repository:
- go to github page, find repository that you want to fork, enter it
- press "Fork" button at the top right corner of the repository
- Now you have a copy that you can work with without impacting it
More information can be found in gitHud Documentation [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
### **(3) Running this Project Locally**
thanks to Anna 

### HEROKU
### **(4) Hosting on Heroku**
Hosting to Heroku you need to go thorugh following steps:
1. Inside git - tell heroku which apps and dependencies are required to run an app - create requirments file abd:

        pip3 freeze --local>requirements.txt   
2. create Procfile for Heroku (important to have space before python and delete last line space in Procfile - it is very important for connection):

        echo web: python app.py>Procfile
NOTE: When deployed the file it is very important that procfile contains very precise inforomation, with no spaces or last emplty line otherwise it won't connect to heroku. 
3. Create new app at heroku profile, app name: ask-pft-meetinghub,
4. Go to heroku website - open the app frim github,  
5. Deploy and enable Automatic Deployment, select "main" branch and press deploy. 
6. After a while - press View - check "hello world"
7. Go to settings and set up config vars:

      IP: "0.0.0.0"
      PORT: "5000"
      SECRET_KEY: (from env.py)
      MONGO_URI: see the step below
      MONGO_DBNAME: "ms3"
8. Hide config vars
9. Check if requiremets.txt and Procfile was created in repository

        CLI: git status
10. Push using commit command for each of the 2 files one by one:

        git add requirements.txt     + Enter
        git commit -m "..."          + Enter
        git add Procfile             + Enter
        git commit -m "..."          + Enter
        git push                     + Enter
11. Connect Mongo DB to heroku as well:
12. In CLI: Install flask-pymongo and dus-python to use mongo srv connection string:
        
        CLI:
        pip3 install flask-pymongo
        pip3 install dns-python

13. Update requirments.txt

        pip3 freeze --local>requirements.txt
14. in app.py install PyMongo and OjectId form the libraries

        from flask_pymongo import PyMongo
        from bson.objectid import ObjectId

15. define app configuration in app.py:

        app.config["MONGO_DBNAME"]= os.environ.get("MONGO_DBNAME")
        app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
        app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

16. Creaete URI key: go to MongoDb, select "databases", go to "connect", go to "connect your application", copy the key and replace 3 parameters;
            
        "mongodb+srv://askformongodb:password@clustername.eqlwe.mongodb.net/databasename?retryWrites=true&w=majority"
        where:
        1. password: XXXXXX
        2. clustername: your_cluster
        3. databasename: your_dtb

#
## CREDITS
### **Content**
  * The conetnt was developed myself based on my experience and thanks to the team from [Alexandr Proudfoot consulting company](https://proudfoot.com/) - Monique, Kamal, Tim Sebastian.

### **Media**
  All the media content was developed by myself in Powerpoint and stored in jpg format

### **Acknowledgements**
  - Code institute for the backend project Example and all the great videos on Python, Flask and database management. Also for github template - I used for code development.
  - Chriss Quin for mentorship
  - Kevin, Miklosh and Johan for great lessons and support during coding problem solving
  - "Alexandr Proudfoot" consulting company for giving me inspiration assigning me to Digital Results Hub workstream and letting me use one of the 5 modules as a prototype for my project
  - Stack overflow and bloggers: 
    - Punit Jajodia and his website [programiz](https://www.programiz.com/python-programming/datetime/current-datetime)
  - My family - for patience, motivation and energy.


## DISCLAIMER
- This project is for educationall purpose only during the Code Institute course of Software Development. Module - Python Flask and Backend development.