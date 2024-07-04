#!/usr/bin/python3
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

# Initialize Flask application instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Bootstrap
bootstrap = Bootstrap(app)

# Import routes and models (assuming they are defined in the app package)
from app import routes, models

# Function to create the app (optional, but useful for testing or modularization)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
