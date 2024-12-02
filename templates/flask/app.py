from flask import Flask, render_template, request

app = Flask(__name__)

#: Use the route() decorator to bind a function to a URL.
@app.route("/")
def index():
    return render_template("index.html")
