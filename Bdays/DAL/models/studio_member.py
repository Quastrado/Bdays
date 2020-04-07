from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from Bdays.DAL.models.db import db
from Bdays.DAL.models.donation import Donation 
#db = SQLAlchemy()


class StudioMember(db.Model):
    __tablename__ = 'studio_members'
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    nickname = db.Column(db.String(50), unique=True)
    birthday = db.Column(db.Date)
    given_donations = db.relationship(
            'Donation', 
            back_populates = 'donation_source',
            foreign_keys = 'Donation.donation_source_id'
            )
    received_donations = db.relationship(
            'Donation',
            back_populates = 'donation_source',
            foreign_keys = 'Donation.donation_target_id'
            )
    