from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/profile/")
def profile():
    return "Profile Page"


app.run()
