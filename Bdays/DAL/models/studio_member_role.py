import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from Bdays.DAL.models.db import db


class StudioMemberRole(db.Model):
    __tablename__ = 'studio_member_roles'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    studio_member_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studio_members.id', ondelete='CASCADE'), nullable=False)
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)

