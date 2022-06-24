# This is my own portofio website

# TODO: Make first draft
# TODO: Write flask app
# TODO: Figure out how to deploy static website

from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from datetime import datetime
import werkzeug
import os

app = Flask(__name__)
Bootstrap(app)

today = datetime.now()
year = today.year

@app.route("/")
def home():
    return render_template('index.html', year=year)

@app.route("/tech-projects")
def tech():
    return render_template('tech_projects.html', year=year)

@app.route("/craft-projects")
def craft():
    return render_template('craft_projects.html', year=year)

@app.route("/links")
def links():
    return render_template('links.html', year=year)

@app.route("/books")
def books():
    return render_template('books.html', year=year)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon/favicon.ico', mimetype='image/vnd.microsoft.icon')


if  __name__ == "__main__":
    app.run(debug=True)