__author__ = 'John Rocha'
__date__ = '2024/11/15'
__contact__ = 'john.rocha@outlook.com'
__version__ = '0.0.1'

#++************************************************************************************************
#+ Understanding:
#++************************************************************************************************
#: In app.py, you’ll find the start of a Flask web application. The application has one route (/)
#: that accepts both POST requests (after the if) and GET requests (after the else). Currently,
#: when the / route is requested via GET, the index.html template is rendered. When the / route is
#: requested via POST, the user is redirected back to / via GET.
#:
#: birthdays.db is a SQLite database with one table, birthdays, that has four columns: id, name,
#: month, and day. There are a few rows already in this table, though ultimately your web
#: application will support the ability to insert rows into this table!
#:
#: In the static directory is a styles.css file containing the CSS code for this web application.
#: No need to edit this file, though you’re welcome to if you’d like!
#:
#: In the templates directory is an index.html file that will be rendered when the user views your
#: web application.
#:


#++************************************************************************************************
#+ Implementation Details:
#+*************************************************************************************************
#: Complete the implementation of a web application to let users store and keep track of birthdays.
#:
#: 1.- When the / route is requested via GET, your web application should display, in a table, all
#:     of the people in your database along with their birthdays.
#:
#:   1.1.- First, in app.py, add logic in your GET request handling to query the birthdays.db
#:         database for all birthdays. Pass all of that data to your index.html template.
#:
#:   1.2.- Then, in index.html, add logic to render each birthday as a row in the table. Each row
#:         should have two columns: one column for the person’s name and another column for the
#:         person’s birthday.
#:
#: 2.- When the / route is requested via POST, your web application should add a new birthday to
#:     your database and then re-render the index page.
#:
#:   2.1.- First, in index.html, add an HTML form. The form should let users type in a name, a
#:         birthday month, and a birthday day. Be sure the form submits to / (its “action”) with a
#:         method of post.
#:
#:   2.2.- Then, in app.py, add logic in your POST request handling to INSERT a new row into the
#:         birthdays table based on the data supplied by the user.
#:
#: Optionally, you may also:
#:
#: a.- Add the ability to delete and/or edit birthday entries.
#:
#: b.- Add any additional features of your choosing!
#:
#:


#++************************************************************************************************
#+ Extra work:
#+*************************************************************************************************
#: While I eventually did add the update and delete functionality, submit will not allow me to
#: submit another html page, which I need in order to do an update.  So I left the initial
#: submission th way it is and the enhanced code here, enhanced.


import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        if not name or not month or not day:
            print("Not enough data")
            return redirect("/")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        return redirect("/")

    else:
        # TODO: Display the entries in the database on index.html
        rows = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=rows)


#: Adding delete functionality
@app.route("/delete/<int:id>")
def delete(id):
    try:
        db.execute("DELETE FROM birthdays WHERE ID = ?",id)
        return redirect("/")
    except:
        return "There was a problem deleting that row"


#: Add update.  To update, we need to add a form to do that.  We can't use the index.html form
#: to do that.  So, we will create a copy of the index.html file and call it update.html and in it
#: we can have the form we need.
#: The one problem I had here is that when I passed row to data, Jinja still treated data as multiple
#: rows although there was only a single row.  Therefore I renamed data to rows so it can read better
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        if not name or not month or not day:
            print("Not enough data")
            return render_template("update.html", rows=row)
        db.execute("UPDATE birthdays SET name = ?, month = ?, day = ? WHERE ID = ?", name, month, day, id)
        return redirect("/")
    else:
        row = db.execute("SELECT * FROM birthdays WHERE ID = ?",id)
        return render_template("update.html", rows=row)





