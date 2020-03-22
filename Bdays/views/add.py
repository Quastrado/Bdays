from flask import render_template, request
from Bdays.forms import BirthdaysForm
from Bdays.models import db, Birthdays

class Add():

    def add_processing(self):
        form = BirthdaysForm()
                
        if request.method == 'POST': 
            if form.add.data:
                if form.validate_on_submit():
                    nickname = form.nickname.data
                    date = form.date.data
                    db_set = Birthdays(nickname = form.nickname.data, date = form.date.data)
                    db.session.add(db_set)
                    db.session.flush()
                    db.session.commit()

        return render_template('add.html', form=form)
