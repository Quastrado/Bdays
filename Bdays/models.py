from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class StudioMembers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(50), unique=True)
    date = db.Column(db.DateTime)


class Donations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer)
    donor = db.Column(db.String(50), unique=True)
    birthday_boy = db.Column(db.String(50), unique=True)
