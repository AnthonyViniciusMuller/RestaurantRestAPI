from flask import Flask
from src.application.routes import routes_blue_print

app = Flask(__name__)

app.register_blueprint(routes_blue_print)