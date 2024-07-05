from flask_sqlalchemy import SQLAlchemy
from app import db

db = SQLAlchemy()

class Source(db.Model):
    __tablename__ = 'sources'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(256))
    category = db.Column(db.String(128))

    # Add more fields as needed

    def __repr__(self):
        return f'<Source {self.name}>'
