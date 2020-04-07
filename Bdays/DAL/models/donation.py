from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from Bdays.DAL.models.db import db

#db = SQLAlchemy()


class Donation(db.Model):
    __tablename__ = 'donations'
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    amount = db.Column(db.Integer)
    donation_source_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studio_members.id'))
    donation_target_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studio_members.id'))
    description = db.Column(db.Text)
    donation_source = db.relationship(
        'StudioMember', 
        foreign_keys = [donation_source_id]
        )
    donation_target = db.relationship(
        'StudioMember', 
        foreign_keys = [donation_target_id]
        )
    
    
