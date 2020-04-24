from flask import current_app as app
from flask import render_template, redirect, request, url_for
from flask import Blueprint
from flask_login import  current_user, login_user, logout_user
from Bdays.DAL.studio_member_repository import StudioMemberRepository


blueprint = Blueprint('login_controller', __name__, static_folder='static')


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    studio_member_repository = StudioMemberRepository()
    nickname = request.form['nickname']
    password = request.form['password']
    studio_member = studio_member_repository.find_studio_member(nickname, password)
    if studio_member:
        login_user(studio_member)
        return url_for('index_controller.dashboard')
    return redirect(url_for('login_controller.login'))

"""
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
"""