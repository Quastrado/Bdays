from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint
from flask_login import current_user
from Bdays.view_models.studio_member import StudioMember as ViewStudioMember, StudioMemberPassword as ViewStudioMemberPassword
from Bdays.DAL.studio_member_repository import StudioMemberRepository
from Bdays.controllers.helper import convert_input_to, exception_handler
from Bdays.services.email_service import EmailSender

from Bdays.exceptions.message_not_send import MessageNotSendError


blueprint = Blueprint('studio_member_controller', __name__, static_folder='static')


@blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    uid = id
    studio_member_repository = StudioMemberRepository()
    studio_member = studio_member_repository.read(uid)
    donators = studio_member_repository.read_all()
    current_user_roles = current_user.roles
    return render_template(
                            'received_donations.html',
                            studio_member=studio_member,
                            donators=donators,
                            current_user_roles = current_user.roles
                            )


@blueprint.route('/', methods=['POST'], endpoint='create_studio_member')
@exception_handler
@convert_input_to(ViewStudioMember)
def create_studio_member(view_studio_member):
    studio_member_repository = StudioMemberRepository()
    studio_member_id = studio_member_repository.create(
            view_studio_member.email,
            view_studio_member.nickname,
            view_studio_member.birthday,
            view_studio_member.role
        )
    sender = EmailSender()
    sender.invite_mail_sender(
        view_studio_member.email,
        studio_member_id
        )
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

    