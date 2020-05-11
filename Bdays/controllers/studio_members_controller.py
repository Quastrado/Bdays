from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint

from Bdays.view_models.studio_member import StudioMember as ViewStudioMember, StudioMemberPassword as ViewStudioMemberPassword
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


@blueprint.route('/', methods=['POST'], endpoint='create_studio_member')
@convert_input_to(ViewStudioMember)
def create_studio_member(view_studio_member):
    studio_member_repository = StudioMemberRepository()
    try:
        studio_member_repository.create(
            view_studio_member.email,
            view_studio_member.nickname,
            view_studio_member.birthday,
            view_studio_member.role
        )
    except Exception as e:
        return 'Internal server error ', 500
    
    return 'Hello', 201


@blueprint.route('/set_password/<id>', methods=['GET'])
def render_set_password(id):
    return render_template('set_password.html', id=id)


@blueprint.route('/set_password', methods=['POST'], endpoint='set_password')
@convert_input_to(ViewStudioMemberPassword)
def set_password(view_studio_member_password):
    studio_member_repository = StudioMemberRepository()
    studio_member_repository.set_password(
        view_studio_member_password.id,
        view_studio_member_password.password
    )
    return '', 201

    