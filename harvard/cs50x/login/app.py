#: Facts:
#:  1.- App allows users to login and remember
#:  2.- Flask "session" allows us to maintain a session/cookie in the browser.  Everyone has their
#:      own
#:  3.- session and therefore unique experience with the server
#:  4.- Flask_session has a class called Session that has methods and allows the instantiation of
#:      a Session object.
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

#: Configuring app is as follows:
#: 1.- app.config["SESSION_PERMANENT"] = False
#:   1.1.- When set to False, when you close the browser, it will loose the session completely
#: 2.- app.config["SESSION_TYPE"] = "filesystem"
#:   2.1.- Stores the cookie information on the server side, not the local browser
#: 3.- Session(app)
#:   3.1.- Applies the configuration changes

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#: First route
@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))

#: Logged in route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
