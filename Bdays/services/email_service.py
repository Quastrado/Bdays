from flask_mail import Mail, Message

from flask import current_app as app
from config import BaseConfig


class EmailSender():

    def invite_mail_sender(self, email, studio_memeber_id):
        mail = Mail(app)
        sender = BaseConfig.MAIL_USERNAME
        recipient = email
        msg = Message('Whellcome', sender=sender, recipients=[recipient])
        msg.body = 'http://127.0.0.1:5000/studio_member/set_password/{}'.format(studio_memeber_id)
        with app.app_context():
            mail.send(msg)