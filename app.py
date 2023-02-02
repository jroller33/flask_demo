from flask import Flask
app = Flask(__name__)\
    
# press Ctrl-shift-p and search python interpreter. then paste the path of 'python.exe' example: (J:\GH Repos\flask_demo\.venv\Scripts\python.exe) paste this into where it asks for the path of the interpreter. this uses the interpreter installed inside the virtual environment. DON'T USE THE SYSTEM PYTHON INTERPRETER! KEEP THE VENV CLEAN

@app.route("/")
def home():
    return "flask is working"