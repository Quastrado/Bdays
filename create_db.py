from Bdays import create_app
from Bdays.models import db

db.create_all(app=create_app())