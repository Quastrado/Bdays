import uuid

from Bdays.DAL.models.db import db
from Bdays.DAL.models.donation import Donation


class DonationRepository():

    def create(self, amount, donation_source, donation_target, description):
        db_set = Donation(
            amount = amount,
            donation_source_id = donation_source,
            donation_target_id = donation_target,
            description = description
            )
        db.session.add(db_set)
        db.session.commit()
        return id


    def read(self, id):
        donation = Donation.query.filter_by(id=id).first()
        return donation


    def read_all(self):
        donations = Donation.query.all()
        return donations


    def update(self, id, amount, donation_source, donation_target, description):
        donation = Donation.query.filter_by(id=id).first()
        donation.amount = amount
        donation.donation_source_id = donation_source
        donation.donation_target_id = donation_target
        donation.description = description
        db.session.commit()


    def delete(self, id):
        db.session.query(Donation).filter(Donation.id == id).delete()
        db.session.commit()
    