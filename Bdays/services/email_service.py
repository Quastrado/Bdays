from flask import request
from flask_mail import Mail, Message

from flask import current_app as app
from config import BaseConfig


class EmailSender():

    def invite_mail_sender(self, email, studio_memeber_id):
        mail = Mail(app)
        sender = BaseConfig.MAIL_USERNAME
        recipient = email
        id = studio_memeber_id
        msg = Message('Wellcome', sender=sender, recipients=[recipient])
        msg.body = f'http://{request.host}/studio_member/set_password/{id}'
        with app.app_context():
            mail.send(msg)