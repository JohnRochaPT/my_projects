from flask import Flask, render_template, request

app = Flask(__name__)
app = Flask(__name__, static_folder='static', static_url_path='/', template_folder='templates')
app.secret_key = 'K5QwCWsJ8qkypg2R3rifHnI0O7'

#: Use the route() decorator to bind a function to a URL.
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
