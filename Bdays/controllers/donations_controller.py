from flask import current_app as app
from flask import render_template
from flask import Blueprint

from Bdays.DAL.donation_repository import DonationRepository
from Bdays.view_models.donation import Donation
from Bdays.controllers.helper import convert_input_to

blueprint = Blueprint('donation_controller', __name__, static_folder='static')


@blueprint.route('/', methods=['POST'])
@convert_input_to(Donation)
def add_donation(donation):
    raise Exception(donation.description)


