from Bdays import create_app
from Bdays.models.db import db
from Bdays.models.studio_member import StudioMember
from Bdays.models.donation import Donation


db.create_all(app=create_app())
