from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint

from Bdays.DAL.studio_member_repository import StudioMemberRepository 


blueprint = Blueprint('index_controller', __name__, static_folder='static')


@blueprint.route('/', methods=['GET'])
def index():
    repo = StudioMemberRepository()
    read_all = repo.read_all()
    nicknames = [nickname for id, nickname, birthday in read_all]
    return render_template('index.html', nicknames=nicknames)