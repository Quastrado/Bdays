# import smtplib
from flask_mail import Mail, Message

from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.models.roles import Role
from Bdays.DAL.models.studio_member_role import StudioMemberRole

from flask import current_app as app 
from config import BaseConfig


class StudioMemberRepository():
    """I am CRUD!"""
    def create(self, email, nickname, birthday, role):
        new_studio_member = StudioMember(
            email = email,
            nickname = nickname,
            birthday = birthday
        )
        studio_memeber_role = db.session.query(Role).filter(Role.role == role).first()
        new_studio_member.role.append(studio_memeber_role)
        db.session.add(new_studio_member)
        db.session.commit()
        
                
        mail = Mail(app)
        sender = BaseConfig.MAIL_USERNAME
        recipient = email
        msg = Message('Whelcome', sender=sender, recipients=[recipient])
        msg.body = "some body"
        with app.app_context():
            mail.send(msg)
        

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


    
        

