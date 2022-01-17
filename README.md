# Cheer you up

General Assembly Software Engineering Immersive - Project 2

Deployment: [here](https://secret-wildwood-49670.herokuapp.com/)

## Project: 

The world is a depressing place.

Your task is to create an app that will allow people to create and share "cheerups" through the `Cheer you up` web app - happy little quips to brighten other people's' days. Cheerups will be small - limited to 139 characters. Members will be able to promote Cheerups that they like and maybe even boost the reputation of the Cheerupper.

## Setup instructions
```
tbc
```


## Technical Requirements:
- [] **Have at *least* 2 tables** (more if they make sense) – one of them should represent the people using your application (users).
- [] **Include sign up/log in functionality (if it makes sense)**, with encrypted passwords & an authorization flow
- [] **Modify data in the database** There should be ways for users to add/change some data in the database (it's ok if only admins can make changes).
- [] Have **semantically clean HTML and CSS**
- [] **Be deployed online** and accessible to the public

## Technology Used
* Python
* HTML
* CSS
* Flask
* PostgreSQL
* Session storage
* Model View Controller Design
TBC

## Minimum Viable Product:
- [x] Users will need to log in/authenticate with a username and password in order to be able to either:
    * Post a 'cheerup'
    * View all existing cheerups that the logged in user has posted
    * Set their main cheerup for their profile (for when others view their profile)
- [x] A session will be used to ensure the user stays logged in
- [x] Only logged in users will be able to '+1' to rate cheerups, which will create a 'cheerup score' (anonymously). The home page will then be sorted based off this score. This will also be used to aggregate the cheerup score of each user
- [x] [API] Set a random avatar for the user with an account
- [ ] Update HTML and CSS to make the web app visually appealing

MVP Relational Database Diagram
![MVP Relational Diagram](/static/images/readme/mvp.png)


## Additional features if time permits:
- [x] [API] Provide the weather for each user based off the users IP address
* Allocate current mood when posting a cheerup
* [API] Allocate a song to their profile ('currently on repeat')
- [x] [API] Add a random joke of the day as an easter egg somewhere on a page 
* Allow users to follow other users cheerups!!
* Allow public and private cheerups
- [x] Display a cheeruper reptuation (i.e. score)

![Additional Features Relational Diagram](/static/images/readme/additional-features-db-diagram.png)


# UI Design:
TBC

Pages 
* Home (main cheerups)
* Login 
* Sign Up
* Profile page (both for logged in users and public)
* Cheerup post page (might use a modal)

# Story Boards:
TBC