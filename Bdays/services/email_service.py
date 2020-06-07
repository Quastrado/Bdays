from smtplib import SMTPDataError, SMTPServerDisconnected

from flask import request
from flask_mail import Mail, Message

from flask import current_app as app
from config import BaseConfig
from Bdays.exceptions.message_not_send import MessageNotSendError


class EmailSender():

    def invite_mail_sender(self, email, studio_memeber_id):
        mail = Mail(app)
        sender = BaseConfig.MAIL_USERNAME
        recipient = email
        id = studio_memeber_id
        msg = Message('Wellcome', sender=sender, recipients=[recipient])
        msg.body = f'http://{request.host}/studio_member/set_password/{id}'
        with app.app_context():
            try:
                mail.send(msg)
                raise MessageNotSendError('Message was not sent. Try again')
            except SMTPDataError as e:
                raise MessageNotSendError('Message was not sent. Try again')
            except SMTPServerDisconnected as e:
                raise e