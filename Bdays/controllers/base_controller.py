from flask import current_app as app
from flask import jsonify, render_template, request
from flask import Blueprint


blueprint = Blueprint('base_controller', __name__, static_folder='static')


class BaseController():

    @blueprint.route('/', methods=['GET'])
    def base():
        return render_template('base.html')