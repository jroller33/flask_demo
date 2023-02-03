import re   # regex used for filtering user input
from datetime import datetime

from flask import render_template


from flask import Flask

app = Flask(__name__)   # creates an instance of FLask
    
# press Ctrl-shift-p and search python interpreter. then paste the path of 'python.exe' example: (J:\GH Repos\flask_demo\.venv\Scripts\python.exe) paste this into where it asks for the path of the interpreter. this uses the interpreter installed inside the virtual environment. DON'T USE THE SYSTEM PYTHON INTERPRETER! KEEP THE VENV CLEAN

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")




@app.route("/hello/")

# <name> is a variable in the URL that's passed to the fn `hello_there(name)` and can be used in the code
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
    
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")