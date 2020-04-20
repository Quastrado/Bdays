from flask import current_app as app
from flask import render_template
from flask import Blueprint


blueprint = Blueprint('login_controller', __name__, static_folder='static')


@blueprint.route('/')
def login():
    return render_template('login.html')