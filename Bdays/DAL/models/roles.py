import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from Bdays.DAL.models.db import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    role = db.Column(db.String(50), unique=True)