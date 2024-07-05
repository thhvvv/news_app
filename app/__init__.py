#!/usr/bin/python3
from flask import Flask
from config import config_options
from app.models import db
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    # Initialize the database with the app
    db.init_app(app)
    bootstrap.init_app(app)

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

from app import routes, models
