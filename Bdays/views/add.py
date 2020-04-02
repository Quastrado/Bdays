from flask import flash, render_template
from Bdays.forms import BirthdaysForm
from Bdays.models import db, StudioMember

class Add():

    def render(self):
        form = BirthdaysForm()
        return render_template('add.html', form=form)
    
    def add_processing(self):
        form = BirthdaysForm()

        if not form.validate_on_submit():
            self.render()
        
        exists = db.session.query(Birthdays.nickname).filter(
                    Birthdays.nickname == form.nickname.data
                    ).scalar()
        if exists is not None:
            #flash('Specified nickname already exists')
            form.nickname.data = ''
            self.render()
            
        nickname = form.nickname.data
        date = form.date.data
        db_set = Birthdays(nickname = form.nickname.data, date = form.date.data)
        db.session.add(db_set)
        db.session.flush()
        db.session.commit()
        return self.render() 
