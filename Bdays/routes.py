from flask import current_app as app
from Bdays.views.add import Add


from Bdays.DAL.studio_member_repository import StudioMemberRepository

@app.route('/add', methods=['GET'])
def add_get():
    add = Add()
    instance = StudioMemberRepository()
    instance.create('67460e74-02e3-11e8-b443-00163e990bdc', '123', '2020-01-01')
    print('idite')
    return add.render()

@app.route('/add', methods=['POST'])
def add_post():
    add = Add()
    return add.add_processing()
