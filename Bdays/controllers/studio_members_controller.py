from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint

from Bdays.DAL.studio_member_repository import StudioMemberRepository


blueprint = Blueprint('studio_member_controller', __name__, static_folder='static')


@blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    uid = id
    studio_member_repository = StudioMemberRepository()
    studio_member = studio_member_repository.read(uid)
    return render_template('received_donations.html', studio_member=studio_member)
    