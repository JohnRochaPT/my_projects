
#;*************************************************************************************************
#;**** Informational sites                                                                   ****
#;*************************************************************************************************

#: Loads the Flask libraries so that they can be used for website building
from flask import Flask, render_template, request

#: Tells Flask that this is the file it needs to run to start the site
app = Flask(__name__)

#: 1.- Use the route() decorator to bind a function to a URL.
#: 2.- The function is what is inside the decorator parenthesis.  For example, with the
#      "@app.route("/")" decorator defines the function that will be called when the URL ends
#      in "/"
#:  2.1.- In this example, the function returns a HTML template called "index.html"
#: 3.- With the decorator "@app.route("/1")", if the URL ends with ..\1, Flask will render
#:     a page that it will build, not using a template, and put in the HTML body, the text
#:     "Number 1 page"
#:@app.route("/")
#:def index():
#:    return render_template("index.html")

#:@app.route("/1")
#:def index1():
#:    return "Number 1 page"

#: 4.- With the decorator "@app.route("/greet")", the function greet() will execute.  It expects
#:     a populated name parameter, which it should have obtained from the @app.route("/") decorator
#:     which calls "index.html".  That page has a form and a submit button which passes a name to
#:     that the Flask "request" class can capture what the user entered in the index.html page and
#:     use it to pass it to the greet.html page which expects a parameter called name passed.
#:  4.1.- The request method behaives differently depending on HTML "forms" method.
#:    4.1.1.- If <..method="get">, use "request.args.get".
#:    4.1.2.- If <..method="post">, use "request.form.get"
#:@app.route("/greet", methods=["POST"])
#:def greet():
#:    name = request.form.get("name", "world")
#:    return render_template("greet.html", name=name)

#: Flask routes can handle multiple items without us having to define multiple routes.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("sport"):
        return render_template("failure.html")
    return render_template("success.html")
