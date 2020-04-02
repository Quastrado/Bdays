from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class StudioMember(db.Model):
    __tablename__ = 'studio_members'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(50), unique=True)
    birthday = db.Column(db.DateTime) 
    

class Donation(db.Model):
    __tablename__ = 'donations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer)
    donation_source = db.Column(db.Integer, db.ForeignKey('studio_members.id'))
    donation_target = db.Column(db.Integer, db.ForeignKey('studio_members.id'))
    description = db.Column(db.Text)
