from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint


blueprint = Blueprint('studio_member_controller', __name__, static_folder='static')


class StudioMemberController():

    @blueprint.route('/add', methods=['GET'])
    def base():
        raise Exception('shtob ti ponyl chto ti zdec')
    