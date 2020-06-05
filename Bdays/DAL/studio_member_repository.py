import uuid

from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.models.roles import Role
from Bdays.DAL.models.studio_member_role import StudioMemberRole


class StudioMemberRepository():
    """I am CRUD!"""
    def create(self, email, nickname, birthday, role):
        new_studio_member = StudioMember(
            email = email,
            nickname = nickname,
            birthday = birthday,
            )
        studio_memeber_role = db.session.query(Role).filter(Role.role == role).first()
        new_studio_member.role.append(studio_memeber_role)
        db.session.add(new_studio_member)
        db.session.commit()
        db.session.refresh(new_studio_member)
        studio_memeber_id = str(new_studio_member.id)
        return studio_memeber_id
       

    def read(self, id):
        studio_member = StudioMember.query.filter_by(id=id).first()
        return studio_member


    def read_all(self):
        studio_members = StudioMember.query.all()
        return studio_members


    def update(self, id, nickname, birthday):
        studio_member = StudioMember.query.filter_by(id=id).first()
        studio_member.nickname = nickname
        studio_member.birtday = birthday
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
        