import uuid

from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint

from Bdays.view_models.studio_member import StudioMember as ViewStudioMember
from Bdays.DAL.studio_member_repository import StudioMemberRepository
from Bdays.controllers.helper import convert_input_to


blueprint = Blueprint('studio_member_controller', __name__, static_folder='static')


@blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    uid = id
    studio_member_repository = StudioMemberRepository()
    studio_member = studio_member_repository.read(uid)
    donators = studio_member_repository.read_all()
    return render_template(
                            'received_donations.html',
                            studio_member=studio_member,
                            donators=donators
                            )


@blueprint.route('/create_studio_member', methods=['POST'])
@convert_input_to(ViewStudioMember)
def create_studio_member(view_studio_member):
    studio_member_repository = StudioMemberRepository()
    new_studio_member_id = uuid.uuid4()
    studio_member_repository.create(
        new_studio_member_id,
        view_studio_member.nickname,
        view_studio_member.birthday,
    )
    print(f'User with id - {new_studio_member_id}')
    return "1" 

    