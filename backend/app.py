from flask import Flask
from portfolio import portfolio
from project import projects

app = Flask(__name__)
app.register_blueprint(portfolio)
app.register_blueprint(projects)