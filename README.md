# Cheer you up

General Assembly Software Engineering Immersive - Project 2

Deployment: [here](https://secret-wildwood-49670.herokuapp.com/)

## Project: 

The world is a depressing place.

Your task is to create an app that will allow people to create and share "cheerups" through the `Cheer you up` web app - happy little quips to brighten other people's' days. Cheerups will be small - limited to 139 characters. Members will be able to promote Cheerups that they like and maybe even boost the reputation of the Cheerupper.

Basic Logic:
* Home (main cheerup view of Top 10 most recent and Top 10 most popular)
* Login (validation check)
* Sign Up:
    * Encrpted passwords
    * Email validation check (i.e. users cannot sign up with the same email)
* Profile page (both for logged in users and public):
    * Users can view their own profile and:
        * Updated their profile (First Name, Last Name, email address, password)
        * Delete and edit their cheerups
        * Find the easter egg (hint 'click' 'Three Cheers' on the top left hand corner)
        * Swap posts from public to private
    * Users can view other peoples profiles and:
        * View publically posted cheerups
        * View the Total Cheerup score of the user
* Cheerups can be posted for every page other than login, signup and 'Cheerupers'
* A page to view all users and their scores in list view, sorted from most popular to least popular
* Posting from a public IP address will invoke a call to the [IP Geolocation API](http://ip-api.com/) to confirm approximate location. A call to [Open Weather Map API](https://api.openweathermap.org/data/2.5) is then invoked to confirm the current weather in that location. This is displayed as additional information to users

## Technology Used
* Python
* HTML
* CSS
* Flask
* PostgreSQL
* Session storage
* Model View Controller Design

# Project Technical Requirements
## Technical Requirements:
- [x] **Have at *least* 2 tables** (more if they make sense) – one of them should represent the people using your application (users).
- [x] **Include sign up/log in functionality (if it makes sense)**, with encrypted passwords & an authorization flow
- [x] **Modify data in the database** There should be ways for users to add/change some data in the database (it's ok if only admins can make changes).
- [x] Have **semantically clean HTML and CSS**
- [x] **Be deployed online** and accessible to the public


## Necessary Deliverables
- [x] A working full-stack application, built by you, hosted somewhere on the internet
- [x] A link to your hosted working app in the URL section of your GitHub repo
- [x] A git repository hosted on GitHub, with a link to your hosted project, and frequent commits dating back to the very beginning of the project. Commit early, commit often.
- [x] A README.md file with explanations of the technologies used, the approach taken, installation instructions, unsolved problems, etc.

### Optional extras
- [x] Use your JavaScript skills to make a smooth UI, e.g. validating your forms before submitting.
- [x] Interact with an external JSON API (check the weather, get book/movie info, space pictures, send SMSs, etc.)


# Planning/Design
## Minimum Viable Product:
- [x] Users will need to log in/authenticate with a username and password in order to be able to either:
    * Post a 'cheerup'
    * View all existing cheerups that the logged in user has posted
    * Set their main cheerup for their profile (for when others view their profile)
- [x] A session will be used to ensure the user stays logged in
- [x] Only logged in users will be able to '+1' to rate cheerups, which will create a 'cheerup score' (anonymously). The home page will then be sorted based off this score. This will also be used to aggregate the cheerup score of each user
- [x] [API] Set a random avatar for the user with an account
- [x] Update HTML and CSS to make the web app visually appealing

MVP Relational Database Diagram:

![MVP Relational Diagram](/static/images/readme/actual-erd.png)


## Additional features if time permits:
- [x] [API] Provide the weather for each user based off the users IP address
- [ ] Allocate current mood when posting a cheerup
- [ ] [API] Allocate a song to their profile ('currently on repeat')
- [x] [API] Add a random joke of the day as an easter egg somewhere on a page 
- [ ] Allow users to follow other users cheerups!!
- [x] Allow public and private cheerups
- [x] Display a cheeruper reptuation (i.e. score)
- [x] Allow user to update their details (first name, last name, email address, password)


# UI Design:
Note: This design changed (for the home screen specifically) half way though the project due to unappealing UI

![General Design](/static/images/readme/general-design.png =100x20) 