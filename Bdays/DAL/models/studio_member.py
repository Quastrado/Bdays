import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from Bdays.DAL.models.db import db
from Bdays.DAL.models.donation import Donation 
from Bdays.DAL.models.roles import Role
from Bdays.DAL.models.studio_member_role import StudioMemberRole
from werkzeug.security import generate_password_hash, check_password_hash


class StudioMember(db.Model, UserMixin):
    __tablename__ = 'studio_members'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.Text(), nullable=False)
    nickname = db.Column(db.String(50), unique=True)
    birthday = db.Column(db.Date)
    password = db.Column(db.String(128))
    role = db.relationship(
        'Role', 
        secondary='studio_member_roles',
        backref=db.backref('studio_member', lazy="dynamic")
        )
    given_donations = db.relationship(
            'Donation', 
            back_populates='donation_source',
            foreign_keys='Donation.donation_source_id'
            )
    received_donations = db.relationship(
            'Donation',
            back_populates='donation_target',
            foreign_keys='Donation.donation_target_id'
            )
    avatar = db.Column(db.Text)

    def set_password(self, password):
        self.password = generate_password_hash(password)
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def roles(self):
        return [role.role for role in self.role]
    