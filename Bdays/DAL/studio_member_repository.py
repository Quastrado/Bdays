from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember


class StudioMemberRepository():
    """I am CRUD!"""
    def create(self, id, nickname, birthday):
        db_set = StudioMember(id = id, nickname = nickname, birthday = birthday)
        db.session.add(db_set)
        db.session.commit()


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