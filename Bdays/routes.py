from flask import current_app as app
from Bdays.views.add import Add


@app.route('/add', methods=['GET'])
def add_get():
    add = Add()
    return add.render()

@app.route('/add', methods=['POST'])
def add_post():
    add = Add()
    return add.add_processing()
