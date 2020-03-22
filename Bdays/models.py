from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Birthdays(db.Model):
    nickname = db.Column(db.String(50), index=True, unique=True, primary_key=True)
    date = db.Column(db.DateTime)