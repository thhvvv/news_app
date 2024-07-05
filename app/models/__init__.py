from flask_sqlalchemy import SQLAlchemy
from .articles import Articles
from .source import Source

# Optionally, you can define __all__ to explicitly specify what is exported
__all__ = ['Articles', 'Source']

db = SQLAlchemy()
