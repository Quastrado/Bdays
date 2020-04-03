from Bdays.models.db import db
from Bdays.models.donation import Donation


class DonationRepository():

    def create(self, id, amount, donation_source, donation_target, description):
        db_set = Donation(
            id = id,
            amount = amount,
            donation_source = donation_source,
            donation_target = donation_target
            )
        db.session.add(db_set)
        db.session.commit()


    def read(self, id):
        donation = Donation.query.filter_by(id=id).first()
        return donation


    def read_all(self):
        donations = Donation.query.all()
        return donations


    def update(self, id, amount, donation_source, donation_target, description):
        donation = Donation.query.filter_by(id=id).first()
        donation.amount = amount
        donation.donation_source = donation_source
        donation.donation_target = donation_target
        donation.description = description
        db.session.commit()


    def delete(self, id):
        db.session.query(Donation).filter(Donation.id == id).delete()
        db.session.commit()
    