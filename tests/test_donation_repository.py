import pytest
import uuid

from tests.test_base import app
from Bdays.DAL.models.db import db
from Bdays.DAL.donation_repository import DonationRepository
from Bdays.DAL.studio_member_repository import StudioMemberRepository

repository = DonationRepository()


"""create method tests"""
def test_donation_create_successfull(client):
    a = uuid.uuid4()
    b = uuid.uuid4()
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    new_donation = repository.create('100', donor, recipient, 'some description')
    assert repository.read(new_donation)
    repository.delete(new_donation)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)
    