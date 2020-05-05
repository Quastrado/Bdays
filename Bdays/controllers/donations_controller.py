from flask import current_app as app
from flask import render_template, request
from flask import Blueprint

from Bdays.DAL.donation_repository import DonationRepository
from Bdays.DAL.models.donation import Donation
from Bdays.view_models.donation import Donation as ViewDonation
from Bdays.controllers.helper import convert_input_to

blueprint = Blueprint('donation_controller', __name__, static_folder='static')


@blueprint.route('/', methods=['POST'])
@convert_input_to(ViewDonation)
def add_donation(view_donation):
    donation_repository = DonationRepository()
    try:
        donation_repository.create(
            view_donation.amount,
            view_donation.donation_source,
            view_donation.donation_target,
            view_donation.description
        )
    except Exception as e:
        return 'Internal server error ', 500
    
    return '', 201
