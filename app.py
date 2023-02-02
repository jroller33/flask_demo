import re   # regex used for filtering user input
from datetime import datetime

from flask import Flask

app = Flask(__name__)   # creates an instance of FLask
    
# press Ctrl-shift-p and search python interpreter. then paste the path of 'python.exe' example: (J:\GH Repos\flask_demo\.venv\Scripts\python.exe) paste this into where it asks for the path of the interpreter. this uses the interpreter installed inside the virtual environment. DON'T USE THE SYSTEM PYTHON INTERPRETER! KEEP THE VENV CLEAN

@app.route("/")
def home():
    return "flask is working"


@app.route("/hello/<name>")
# <name> is a variable in the URL that's passed to the fn `hello_there(name)` and can be used in the code
# http://127.0.0.1:5000/hello/john returns "Hello there john! It's Wednesday, 01 February, 2023 at 20:18:53"


def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    
    # filter name arg to letters only using regex (so user can't paste HTML etc)
    # URL args can contain any text, so restrict to safe chars only
    
    match_object = re.match("[a-zA-Z]+", name)
    
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
        
    content = str(f"Hello there {clean_name}! It's {formatted_now}")
    return content

