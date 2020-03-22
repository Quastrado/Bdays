from flask import current_app as app
from Bdays.views.add import Add


@app.route('/add', methods=['GET','POST'])
def add():
    add = Add()
    return add.add_processing()

