#!/usr/bin/python3
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

from app import routes, models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
