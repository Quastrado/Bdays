from flask import current_app as app
from flask import jsonify, redirect, render_template, request, url_for
from flask import Blueprint
from flask_login import current_user, login_required

from Bdays.DAL.studio_member_repository import StudioMemberRepository
from Bdays.DAL.role_repository import RoleRepository


blueprint = Blueprint('index_controller', __name__, static_folder='static')


@blueprint.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index_controller.dashboard'))
    return render_template('index.html')


@blueprint.route('/dashboard')
@login_required
def dashboard():
    studio_member_repository = StudioMemberRepository()
    role_repository = RoleRepository()
    studio_members = studio_member_repository.read_all()
    roles = role_repository.read_all()
    current_user_roles = current_user.roles
    return render_template('base.html',
                            studio_members=studio_members,
                            roles=roles,
                            current_user_roles=current_user_roles
                            )
