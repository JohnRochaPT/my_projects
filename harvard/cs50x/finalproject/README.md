
# SmartShots Survey Tracker
In this final CS50x assignment, my main objective is to demonstrate the **ability to implement** of most concepts and techniques taught in the CS50's Introduction to Computer Science course. In this assignment, I will implement a solution that addresses the below user story.
> **Note:** This readme file has essentially **two sections**.  The first section is more of a summary section designed to allow the reader to gain a high level understanding of the solution the program tries to resolve and the approach.   It then proceeds to a more detail section where the task is broken down further.

#### Video Demo:  <[CS50x Final Project](https://youtu.be/iD4RNIjC0xE) >

## Accunts:

 - **edx** ⇒ LearnForEverNow
 - **edx** ⇒ LearnForEverNow


## Files in root folder

 - **app.py** ⇒ This is the main application file
 - **helpers.py** ⇒ This is a helper python file containing functions I use
 - **requirements.txt** ⇒ This file contains all the libraries the project needs
 - **sql1ddl.txt** ⇒ File contains sql snippets I use to develop the project
 - **surveys.db** ⇒ This is the sqlite3 database used in this project
 - **readme.md** ⇒ This file

## Files in flask_session
 - **all files** ⇒ If there are any files here, they will be from old running server side sessions

## Files in static\css
 - **style.css** ⇒ This is my own css style file for all my HTML templates
 - **all other files** ⇒ All other files represent a local installation of Bootstrap

## Files in static\img
 - **all files** ⇒ Application images

## Files in static\js
 - **all files** ⇒ Javascript files for bootstrap and for me

## Files in templates
 - **layout.html** ⇒ This is the main HTML page that is inherited from all other pages
 - **index.html** ⇒ This is th home landing page
 - **error.html** ⇒ Page dedicated to present critical error to the user, as opposed to having unintelligent internal errors
 - **addSurvey.html** ⇒ This page is used by Administrators to add surveys to the application
 - **login.html** ⇒ Page allows users to login as well as request for a password reset
 - **register.html** ⇒ Page allows users to create a user's account
 - **request_reset.html** ⇒ This page allows users to request for a password reset
 - **reset_password.html** ⇒ This page consumes the email token sent to the user when a user wants to change their password
 - **surveys.html** ⇒ Page illustrates all the surveys user has taken
 - **takeSurveys.html** ⇒ Page allows users to register to a survey and begin taking that survey


## Brief User Story:
This project will actually be used as a real **Production Project** for Joseph Brusatto from OneMedical.  Joseph is in the process
of completing his Doctor of Nursing Practice Student's degree from Herzin.  He is required to implement a project that can be used
at OneMedical which provides a benefit to providers.  His project includes vaccine decision support dashboard which facilitates children vaccines.  To complete his project, he is required to have all providers complete 3 surveys and then collect that information and show the overall benefits of SmartShots, his application.

My project allows OneMedical providers to create an account, complete and track all their surveys.  Part of the requirements is that the Joe cannot tie a user to a survey.  All the surveys **have to be anonymous**.  There will be approx 2,500 users using the application for about 3 months.

# Detailed Section
The application will allow OneMedical doctors to monitor their survey and has the following requirements:

 - **Hashed Users ID** - All accounts have to be anonymous.  That essentially means that their user id, which is required to be a OneMedical email address, must be stored in the database hashed.
 - **User authentication** - When a user connects to the application, the app compares their email address to the user's table hashed user ids.
 - **Hashed Passwords** -  Passwords must be hashed
 - **App Security** -
	 - Must use app secret key
	 - Sessions store key information
	    - Stored on the server side
	    - Sessions are encrypted
	    - Sessions expire in 30 days
	 - When a user selects a survey, the application must launch an survey page (external) using a unique url ID given to each users
	    - This unique number is different than their user IDs and is randomly generated
	 - Password changes must use email
	    - When a user requests a password change, the application needs to use send an email to the user with an encrypted token
	    - Token must be time aware and not exceed more than 5 minutes
 - **Application Administration** - The application needs to include administration functionality.  Includes:
	 - A screen where administrators can define the properties of surveys including the survey's URL
	 - Administrators need to be able to inactivate surveys.
 - **User friendly Messages** - Application multiple approaches to keep the user informed. As follows:
 	 - Uses Flask Flash messages to inform the user when something happens, such as they successfully logged in.
 	 - In the event of Internal Errors or critical errors, the application handles them gracefully by presenting an error page
 - **Uses Jinja2 HTML Templates** - Advanced Jinja2 HTML pages including the hiding and presentation of admin menus when applicable



