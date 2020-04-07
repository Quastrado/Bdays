from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint


blueprint = Blueprint('studio_member_controller', __name__, static_folder='static')


@blueprint.route('/uid', methods=['GET'])
def uid():
    uid = request.args.get('studio_member_id')
    return(uid)
    