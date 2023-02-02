import re   # regex used for filtering user input
from datetime import datetime

from flask import render_template


from flask import Flask

app = Flask(__name__)   # creates an instance of FLask
    
# press Ctrl-shift-p and search python interpreter. then paste the path of 'python.exe' example: (J:\GH Repos\flask_demo\.venv\Scripts\python.exe) paste this into where it asks for the path of the interpreter. this uses the interpreter installed inside the virtual environment. DON'T USE THE SYSTEM PYTHON INTERPRETER! KEEP THE VENV CLEAN

@app.route("/")
def home():
    return "flask is working"


# <name> is a variable in the URL that's passed to the fn `hello_there(name)` and can be used in the code
# http://127.0.0.1:5000/hello/john returns "Hello there john! It's Wednesday, 01 February, 2023 at 20:18:53"


@app.route("/hello/")

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