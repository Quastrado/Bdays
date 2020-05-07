import smtplib

from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.models.roles import Role
from Bdays.DAL.models.studio_member_role import StudioMemberRole

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

        mail_user = BaseConfig.GMAIL
        mail_password = BaseConfig.GMAIL_PASSWORD
        
        sent_from = mail_user
        to = email
        subject = 'Set your password'
        body = 'URL must be here'

        email_text = """
        From: %s
        To: %s
        Subject: %s

        %s 
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(mail_user, mail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        except Exception as e:
            return e


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


    
        

