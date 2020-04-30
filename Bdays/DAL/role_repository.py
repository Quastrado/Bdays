from Bdays.DAL.models.db import db
from Bdays.DAL.models.roles import Role


class RoleRepository():

    def create(self, id, role):
        db_set = Role(
            id = id,
            role = role
            )
        db.session.add(db_set)
        db.session.commit()
        return id


    def read(self, id):
        role = Role.query.filter_by(id=id).first()
        return role


    def read_all(self):
        roles = Role.query.all()
        return roles


    def update(self, id, role):
        role = Role.query.filter_by(id=id).first()
        role.role = role
        db.session.commit()


    def delete(self, id):
        db.session.query(Role).filter(Role.id == id).delete()
        db.session.commit()
