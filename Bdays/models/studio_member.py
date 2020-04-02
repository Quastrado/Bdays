from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from Bdays.models.db import db

#db = SQLAlchemy()


class StudioMember(db.Model):
    __tablename__ = 'studio_members'
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    nickname = db.Column(db.String(50), unique=True)
    birthday = db.Column(db.DateTime)
    