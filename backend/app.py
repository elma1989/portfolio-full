from flask import Flask
from project import projects

app = Flask(__name__)
app.register_blueprint(projects)