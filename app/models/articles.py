from flask_sqlalchemy import SQLAlchemy
from app import db

db = SQLAlchemy()

class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(128))
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(256))
    urlToImage = db.Column(db.String(256))
    publishedAt = db.Column(db.String(128))
    content = db.Column(db.Text, nullable=False)

    # Add more fields as needed

    def __repr__(self):
        return f'<Article {self.title}>'
