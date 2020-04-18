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
    donation = Donation()
    donation.amount = view_donation.amount
    donation.description = view_donation.description
    print(view_donation.amount, view_donation.description)
    return '1'
