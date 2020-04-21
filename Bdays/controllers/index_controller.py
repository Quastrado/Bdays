from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint
from flask_login import login_required

from Bdays.DAL.studio_member_repository import StudioMemberRepository


blueprint = Blueprint('index_controller', __name__, static_folder='static')


@blueprint.route('/', methods=['GET'])
def index():
    # studio_member_repository = StudioMemberRepository()
    # studio_members = studio_member_repository.read_all()
    return render_template('index.html')#, studio_members=studio_members)


@blueprint.route('/dashboard')
@login_required
def dashboard():
    studio_member_repository = StudioMemberRepository()
    studio_members = studio_member_repository.read_all()
    return render_template('base.html', studio_members=studio_members)