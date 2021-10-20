# GROCS

![screenshot landing desktop](assets/img/screenshots/screenshot_items_desktop.png)

# MP3
Milestone project 3

### User Stories

## User Experience (UX)
* First time visitor goals
	* As a first time visitor, I want to instantly understand the main purpose of the site: to keep grocery lists.
	* As a first time visitor I want to be able to sign up quickly and start using this website.
* Returning visitor goals
	* As a returning visitor, I want to access the list that I left on my last visit. 
* Frequent user goals
	* As a frequent visitor I want to be able to quickly view and make changes to the list I left before. 

### Design
* Colour Scheme
	* For the colour scheme white, black, teal and light amber are used. The amber is used to resemble the colour of paper or a postit note. 
* Typography
	* The main font family used is Roboto Mono, which falls back onto monospace if unavailable. 
	* The secondary font family that is used for titles is Permanent Marker, which falls back onto cursive if unavailable. 


### Wireframes
| Login page mobile | List page mobile |
| ---------------- | --------------- |
| ![Login page mobile](assets/img/wireframes/wireframe_mobile_main.png) | ![homepage wireframe mobile](assets/img/wireframes/wireframe_mobile_list.png) |

## Features
* Responsive on mobile device as well as desktop sizes.
* No Personal Identifiable Information from the user is taken into this project. 
* Privacy is granted by using Werkzeug privacy features.
* CRUD functionality with database.  


## Technologies used

### Languages used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used
* [Google Fonts](https://fonts.google.com/)
	* Goole Fonts were used to import the Permanent Marker and the Roboto Mono fonts into the style.css file. This is used on all pages of the project.
* [Font Awesome](https://fontawesome.com/)
	* Font Awesome was used for the icon elements on the registration page.
* [Wireframes|cc](https://wireframe.cc)
	* Wireframes|cc is used for the initial wireframes.
* [Materialize](https://materializecss.com)
	* Materialize was used for the front end framework. 
* [MongoDB](https://www.mongodb.com/)
	* MongoDB was used as the database for this project.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
	* Flask was used to build this python application and for template enheritance. 
* [Werkzeug](https://pypi.org/project/Werkzeug/)
	* Werkzeug was used to facilitate secure log in.
* [Heroku](http://www.heroku.com)
	* Heroku was used to connect the database to the application.

## Testing

The testing of CSS and HTML was done through W3C markup Validator and the W3C CSS Validator Services. The page was tested and validated only with errors related to Flask elements, which are expected. Python code was tested for PEP8 compliance through TutorialPoint

* [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
* [W3C Nu HTML Checker](https://validator.w3.org/nu/#textarea)
* [TutorialPoint](https://www.tutorialspoint.com/online_python_formatter.htm)
* JavaScript was tested through [JSHint](https://jshint.com) and returned no errors.

### Further testing

Further testing was done manually.
* I have checked and clicked back on forth on all href elements on both desktop as well as mobile sizes on both Chrome and Safari with the intent to try to break the system.
* For first time user user stories, I have asked friends to try this website without any further instructions. There were no major bugs found and UI was found to be non-ambiguous and easy to follow.
* Testing for responsiveness and other has been done on both desktop as well as mobile sizes on both Chrome and Safari.
* All functions have been further tested.

### Known bugs
* A major shortcoming for this application is the data types used. Ideally, categories should include the items in one structure. If I had to restart this project, I would take a different approach here.
* No functionality is in place at the moment to remove a user and associated items. This can be added at a later stage but was deemed unnecessary by my mentor for now.
* Initialising of items takes a long time. Ideally a visual aid should be shown to indicate that initialisation is in progress.
* Wireframes for homepage got lost.

## Deployment

### Private website

The website is deployed on Google Cloud and hosted on my personal website (jildourixt.nl). It is also hosted on [34.116.200.121](http://34.118.58.167/home)

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/jildourixt/grocs.git)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/jildourixt/grocs.git)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
``` 
$ git clone https://github.com/jildourixt/grocs.git
```
7. Press Enter. Your local clone will be created.

## Credits

### Acknowledgements
* My mentor for continuous helpful feedback.
* Tutor support at Code Institute for their support and materials.
* The inital structure for this project is heavily based on the mini project of the Code Institute for the Milestone 3 project. Further implementation for functionality is added on top of this. Many thanks and credits for this. 