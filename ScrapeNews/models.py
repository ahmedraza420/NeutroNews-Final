from enum import unique
from ScrapeNews import db
from datetime import datetime

class UpToDateNews(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    newsTitle= db.Column(db.String(200), nullable=False)
    newsText = db.Column(db.String(200000), nullable=False)
    newsUrl = db.Column(db.String(1000), nullable=False)
    newsImage = db.Column(db.String(1000), unique=False,nullable=False)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)
    sentiment= db.Column(db.String(25), default='neutral')
    category = db.Column(db.String(30), default='Others')

    def __repr__(self):
        return f"UpToDateNews {self.newsTitle}, {self.newsText}, {self.newsUrl}, {self.newsImage}, {self.id}, {self.date_created}, {self.sentiment}, {self.category}"

class HotNews(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    newsTitle= db.Column(db.String(200), nullable=False)
    newsUrl = db.Column(db.String(1000), nullable=False)
    newsImage = db.Column(db.String(1000), nullable=False)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"HotNews('{self.newsTitle}, {self.newsUrl}, {self.newsImage}, {self.id}')"