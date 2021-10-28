# MS3 - Management Operating System (MOS) - Meetings Hub

## **Introduction**
  A "Meetings Hub" project is a web application to digitalise an effective performance management via structured meetings focused on Key Performance Indicators (KPIs) and corrective actions. The app is built based on one of the modules of "Digital Results Hub"(DRH) - a solution developed for a real consulting company. This module helps to digitise  Management Operatiing System (MOS) elements of the consulting methodology. 
  "Meeitngs Hub" is a part of more extensive solution that was developed in 2021 by a global consulting company. Initial solution consists of 4 modules and "Meetings Hub" is one of 4 modules.
  "Meeitngs Hub" consists of meetings, KPIs adn actions reviewed during the meetings. Meeting Hub solution is a digital product that is normally installed at the client's site. It helps the client to improve meetings quality and manage productivity through standard process of looking at performance trends and defiining actions to address the variance between plananed and actual performance. 
  hwen started the application was built for educational purposes only.

Link to the Application: [DRH-MOS]()

Super Admin access:
    * _Login_: TBD; 
    * _Password_: TBD;
#

## **User Experience (UX)**
### GOALS
1. **For user** - the application will help a meeting chair to navigate thorugh KPIs Viusuals during the meeting, by using filters KPIs will be filtered by accountability. The performance of each participant will be visualised through Key Perrformance Indicators and those KPIs that require action effort will be conditionally highlighted. The visualisation will help to quickly identify the preformance level and address the variance with actions assigned to meeting participants.
2. **For Meeting participants** - the appliaction will help to understand through KPIs where they are expected to report to their meeting chair, suggest corrective actions, systematically follow up on actions and communicate actions completion during the meeting.
3. **For user with admin right** - the application will help the user with admin rihgths (secretary) to administer inputs for KPIs, inputs for actions, update actions statuses. That will be done prior to the meetings defined in applications
4. **For all the client's participants** - it will help to register and login to obtain an access to a set of performance indicators to manage department effectiveness and report performance throguh KPIs during the meeting. 
5. **For a developer** - the application is a simultaion of a real product that is currently in demand from industrial clients - large scale organisations with several levels of management. This app will help the developer to demosntrate the developer skills for potential emloyer that employ developer for consulting service. It can potentially be sold to his current employer who currently develops Digital Results HUb using other platforms (Azure, Power Bi etc.)


### USER STORIES
#### As a Site User
  - _USER STORY 1_: The admin user registers with super admin rights, 
  - _USER STORY 2_: The admin user defines MOS system elements parameters: roles,  participants, participants rights, meetings structure, meetings inputs parameters (KPIs and Actions), define accountability for teh KPIs and Atcions
  - _USER STORY 4_: The admin user prepare for the meeting prior to the meeting: update KPIs inputs, update action Status inputs, 
  - _USER STORY 5_: The admin user enters new actions after each meeting based on results of the meeting
  - _USER STORY 5_: each meeting participant can navigate through meeting dashboard
  - _USER STORY 5_: each meeting participant can use tablet or mobile to look at the dashboard and prepare for the meeting
  - _USER STORY 6_: The admon is able to navigate during the meeting using filters on the dashboard to facilitate the dicussion between participants during te meeting.
  - _USER STORY 6_: The information is enetered to the cloud based non-relational database and can ve accessed by the developer

#### As an Appliaction Buyer
  - _USER STORY 7_: Consulting company who sees the product adding value to the methodolgy is willing to integrate this application into their Digital Results Hub 

#### As a Developer
  - _USER STORY 8_: Developer wants to copy the app code to sell it to a consulting company that currently employ developer or to sell it in the future.
  - _USER STORY 9_: Developer can use an app to show how software development skils can add value to consulting skills. Tha consulting approach can be digitalised. 

### DESIGN PROCESS
* _Strategy Plain_: 
    * The application is a product for the client. The client shall own a database and needs to be able to migrate to any platform that he wants to.
    * From another side, the client can just use the appliactin without knowing what it consists of.
    * There will be 3 levels of rights - super admin, admin and user
    * the application can be used for 1 department fr organisation or for multisite organsiation
* _Scope Plain_: 
    * The table below defines the scope, user rights and access to various application components:

        No. | Category                                | Super Admin rights  | Admin rights | User rights
        ----|---------                                | ------| ----| -----
        01  | Register                                |Yes    |Yes  | Yes 
        02  | Login                                   |Yes    |Yes  | Yes 
        03  | Set up Organisation levels              |Yes    |Yes  | No
        03  | Set up users rights                     |Yes    | No  | No
        04  | Set up roles                            |   Yes | No  | No 
        05  | Set up participants                     |   Yes | Yes | No 
        06  | Set up meeting types                    |   Yes | Yes | No   
        07  | Set up meeting content                  |   Yes | Yes | No   
        08  | Set up KPIs                             |   Yes | Yes | No  
        09  | Set up/Edit Action Log parameters       |   Yes | Yes | No  
        10  | Design Visual Dashboard in BI platform  |   Yes | No  | No     
        10  | Define inputs for visual dashboard      |   Yes | No  | No     
        11  | Filter Visual Dashboard parameters      |   Yes | Yes | Yes  
        12  | Update KPI inputs prior to the meeting  |   Yes | Yes | No   
        13  | Edit KPI inputs at any tiime            |   Yes | No  | No  
        14  | Update Actions completion status        |   Yes | Yes | No 
        15  | Update New Actions into action log      |   Yes | Yes | Yes  
        16  | Archive Meeting dashboard as pdf        | Yes   | Yes | No
  
    * The table below defines what will be deeloped with an application scope
        IN Scope | NOT in Scope
        ---------|--------- 
        Cleint login |  
        User registration |  
        KPI Input updates |  
        New Actions updates |  
        Actions status updates |  
        Dashboard navigation |  
        x | Dashboard design
        x | Connecting to the client Database
        Stoing data inputs on the cloud storage | 
        CRUD Functionality for Actions |
        CRUD Functionality for KPIs |
        CRUD Functionality for Users, participants and roles |
        Database storage |
  

* _Structure Plain_:
  * Link to [Structure](static/img/structure.jpg) - the structure was built in MS PowerPoint
  * Link to [Schema](static/img/schema.jpg) - the schema was built in Power BI.
* _Skeleton Plain_:
  * [Link to responsive Wireframe file in pdf](https://drive.google.com/file/d/1fsWrmySpizFI2vYiG_p664LLvPUs-nNF/view?usp=sharing)
![wireframe](static/img/wireframe.jpg)
* _Surface Plain_:
Website colors and design team will be simple and neutral, it means - limited amount of colors. Colors focused onlly in higlights. 
  * Colour Pallette 
  _Source_: Materialise

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
    Contrast Icons|blue-grey darken-1|#546e7a
    Non-contracts Icons|blue-grey lighten-4| #cfd8dc



  * Fonts
  I will use traditional business fonts - "Roboto" and "Sans Serif", or Lato and PT Sans.

### FEATURES
  * Existing Features
    - xxx
  * Features left to Implement
    - Login page with basic security functionality
    - Register page with basic security requirements
    - User rights
    - Navbar
    - Sidebar for mobile version
    - Spycroller
    - Input form
    - Search
    - Charts Dashboards
    - Modals warning about irreversibility of operation (delete, edit etc.)

### TECHNOLOGIES
  * Languages
    - HTML
    - CSS
    - Javascript
    - Python
    - Jinja
  * Libraries
    - Flask
    - Materialize
    - FontAwesome
    - JQuery
  * API's
    - Power BI for Dashboard
    - Mongo DB connector to Power BI
  * - Databases 
    - Mongo DB - non-relational database
  * Tools
### TESTING [link](link to anoher .md file)
  ### Navigation
  ### Browser Compatibilty
  ### Responsiveness
  * User stories testing
  * User stories testing
  * Validation of Code Testing
    - [HTML]
    - [CSS]
    - [JavaScript]
    - [Python]
  * Lighthoouse for Site Performance
## DEPLOYMENT
  * Hosting on Heroku
  * Hosting on GitHub pages
      - Used Commands during Deployment
  * Forking the GitHub Repository
  * Running this Project Locally

## CREDITS
  * Content
  * Media
  * Acknowledgements

## DISCLAIMER