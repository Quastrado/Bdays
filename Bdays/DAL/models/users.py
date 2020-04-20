from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from Bdays.DAL.models.db import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(10), index=True)


    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)