from Bdays.models.db import db
from Bdays.models.studio_member import StudioMember
from datetime import datetime as dt


class StudioMemberRepository():

    def create(self, id, nickname, date):
        my_date = dt.strptime(date, '%Y-%m-%d')
        db_set = StudioMember(id = id, nickname = nickname, birthday = my_date)
        db.session.add(db_set)
        db.session.commit()