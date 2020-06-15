import pytest
import uuid

from sqlalchemy.exc import DataError

from tests.test_base import app
from Bdays.DAL.models.db import db
from Bdays.DAL.donation_repository import DonationRepository
from Bdays.DAL.studio_member_repository import StudioMemberRepository

repository = DonationRepository()


"""create method tests"""
def test_donation_create_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    new_donation = repository.create('100', donor, recipient, 'some description')
    assert repository.read(new_donation)
    repository.delete(new_donation)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_incorrect_amount(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    with pytest.raises(DataError):
        new_donation = repository.create('abc', donor, recipient, 'some description')
    db.session.rollback()
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_no_donor(client):
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    with pytest.raises(TypeError):
        new_donation = repository.create('abc', recipient, 'some description')
    StudioMemberRepository().delete(recipient)


def test_no_recipient(client):
    donor = StudioMemberRepository().create('email2@dot.com', 'donor', '01.01.2000', 'Studio Member')
    with pytest.raises(TypeError):
        new_donation = repository.create('abc', donor, 'some description')
    StudioMemberRepository().delete(donor)


"""read method tests"""
def test_read_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    assert repository.read(donation_id)
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_read_missing_id(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    with pytest.raises(TypeError):
        repository.read()
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


"""read all method tests"""
def test_read_all_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    donation = repository.read(donation_id)
    all_donations = repository.read_all()
    assert donation in all_donations
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)

