from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired


class BirthdaysForm(FlaskForm):
    nickname = StringField('Nickname:', validators=[DataRequired()], render_kw={"class": "form-control"})
    date = DateField('Date:', format='%m.%d', validators=[DataRequired()], render_kw={'placeholder': '00.00',
                                                                                        "class": "form-control"
                                                                                        })
    add = SubmitField('Add', render_kw={"class": "btn btn-secondary"})
