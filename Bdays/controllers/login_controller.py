from flask import current_app as app
from flask import render_template, redirect, request, url_for
from flask import Blueprint
from flask_login import  current_user, login_user, logout_user
from Bdays.DAL.models.users import User


from Bdays.DAL.user_repository import UserRepository


blueprint = Blueprint('login_controller', __name__, static_folder='static')


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    user_repository = UserRepository()
    username = request.form['username']
    password = request.form['password']
    user = user_repository.find_user(username, password)
    if user:
        login_user(user)
        return url_for('index_controller.dashboard')
    return redirect(url_for('login_controller.login'))


@blueprint.route('/process-registration', methods=['POST'])
def process_registration():
    user_repository = UserRepository()
    username = request.form['username']
    password = request.form['password']
    password_replay = request.form['password_replay']
    if password == password_replay:
         user_repository.registration(username, password)
         return url_for('index_controller.index')
    return url_for('index_controller.registration')