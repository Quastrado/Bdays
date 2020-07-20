import re
import uuid
from flask_mail import Mail, Message

from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.models.roles import Role
from Bdays.DAL.models.studio_member_role import StudioMemberRole

from flask import current_app as app 
from config import BaseConfig


class StudioMemberRepository():
    """I am CRUD!"""
    def create(self, studio_member_dto, role):
        check_email = re.match(r'\w+@\w+', studio_member_dto.email)
        if not check_email:
            raise ValueError
        new_studio_member = StudioMember(
            email=studio_member_dto.email,
            nickname=studio_member_dto.nickname,
            birthday=studio_member_dto.birthday
        )
        studio_memeber_role = db.session.query(Role).filter(Role.role == role).first()
        new_studio_member.role.append(studio_memeber_role)
        db.session.add(new_studio_member)
        db.session.commit()
        studio_memeber_id = str(new_studio_member.id)
        print(type(studio_memeber_id))
        return studio_memeber_id
       

    def read(self, id):
        studio_member = StudioMember.query.filter_by(id=id).first()
        return studio_member


    def read_all(self):
        studio_members = StudioMember.query.all()
        return studio_members


    def update(self, id, studio_member_dto):
        studio_member = StudioMember.query.filter_by(id=id).first()
        dto = studio_member_dto
        data = dto.__dict__
        for k, v in data.items():
            setattr(studio_member, k, v)
        db.session.commit()
    

    def delete(self, id):
        db.session.query(StudioMember).filter(StudioMember.id == id).delete()
        db.session.commit()
    

    def find_studio_member(self, nickname, password):
        studio_member = StudioMember.query.filter(StudioMember.nickname == nickname).first()
        if studio_member and studio_member.check_password(password):
            return studio_member


    def set_password(self, id, password):
        studio_member = StudioMember.query.filter_by(id=id).first()
        studio_member.password = studio_member.set_password(password)
        db.session.commit()
    