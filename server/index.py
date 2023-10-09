# pip install requirements.txt - before making a change
# place package name into requirements.txt file when downloaded

from flask import Flask
from flask_cors import CORS, cross_origin
from jinja2 import FileSystemLoader
from latex.jinja2 import make_env
from latex import build_pdf

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome to resume-latex</h1>"


if __name__ == '__main__':
    app.run()

