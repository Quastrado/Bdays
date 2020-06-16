import pytest
import uuid

from sqlalchemy.exc import DataError, ProgrammingError

from tests.test_base import app
from Bdays.DAL.models.db import db
from Bdays.DAL.donation_repository import DonationRepository
from Bdays.DAL.studio_member_repository import StudioMemberRepository

repository = DonationRepository()


"""create method tests"""
def test_create_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    new_donation = repository.create('100', donor, recipient, 'some description')
    assert repository.read(new_donation)
    repository.delete(new_donation)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_create_incorrect_amount(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    with pytest.raises(DataError):
        new_donation = repository.create('abc', donor, recipient, 'some description')
    db.session.rollback()
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_create_no_donor(client):
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    with pytest.raises(TypeError):
        new_donation = repository.create('abc', recipient, 'some description')
    StudioMemberRepository().delete(recipient)


def test_create_no_recipient(client):
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


def test_read_incorrect_id(client):
    with pytest.raises(ProgrammingError):
        repository.delete(231421141432)


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


"""update method test"""
def test_update_amount_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_amount = '200'
    repository.update(donation_id, another_amount, donor, recipient, 'some description')
    donation = repository.read(donation_id)
    assert donation.amount == 200
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_update_description_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_amount = 'another description'
    repository.update(donation_id, '100', donor, recipient, another_amount)
    donation = repository.read(donation_id)
    assert donation.description == 'another description'
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_update_donor_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_donor = StudioMemberRepository().create('mail@dot.com', 'another donor', '01.01.2000', 'Studio Member')
    repository.update(donation_id, '100', another_donor, recipient, 'some description')
    donation = repository.read(donation_id)
    assert str(donation.donation_source_id) == another_donor
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(another_donor)
    StudioMemberRepository().delete(recipient)


def test_update_recipient_successfull(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_recipient = StudioMemberRepository().create('mail@dot.com', 'another recipient', '01.01.2000', 'Studio Member')
    repository.update(donation_id, '100', donor, another_recipient, 'some description')
    donation = repository.read(donation_id)
    assert str(donation.donation_target_id) == another_recipient
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)
    StudioMemberRepository().delete(another_recipient)


def test_update_missing_id(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_amount = '200'
    with pytest.raises(TypeError):
        repository.update(another_amount, donor, recipient, 'some_description')
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_update_missing_amount(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    with pytest.raises(TypeError):
        repository.update(donation_id, donor, recipient, 'some_description')
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_update_missing_donor(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_amount = '200'
    with pytest.raises(TypeError):
        repository.update(donation_id, another_amount, recipient, 'some_description')
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_update_missing_recipient(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_amount = '200'
    with pytest.raises(TypeError):
        repository.update(donation_id, another_amount, donor, 'some_description')
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_update_missing_description(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    another_amount = '200'
    with pytest.raises(TypeError):
        repository.update(donation_id, another_amount, donor)
    repository.delete(donation_id)
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


"""delete method test"""
def test_delete_successful(client):
    donor = StudioMemberRepository().create('email@dot.com', 'donor', '01.01.2000', 'Studio Member')
    recipient = StudioMemberRepository().create('email2@dot.com', 'recipient', '01.01.2000', 'Studio Member')
    donation_id = repository.create('100', donor, recipient, 'some description')
    repository.delete(donation_id)
    assert repository.read(donation_id) == None
    StudioMemberRepository().delete(donor)
    StudioMemberRepository().delete(recipient)


def test_delete_missing_id(client):
    with pytest.raises(TypeError):
        repository.delete()


def test_delete_incorrect_id(client):
    with pytest.raises(ProgrammingError):
        repository.delete(76189613)
