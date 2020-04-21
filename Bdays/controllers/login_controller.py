from flask import current_app as app
from flask import render_template, redirect, request, url_for
from flask import Blueprint
from flask_login import  current_user, login_user, logout_user
from Bdays.DAL.models.users import User


blueprint = Blueprint('login_controller', __name__, static_folder='static')


@blueprint.route('/login')
def login():
    return render_template('login.html')


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter(User.username == username).first()
    if user and user.check_password(password):
        login_user(user)
        return url_for('index_controller.dashboard')

    return redirect(url_for('login'))
