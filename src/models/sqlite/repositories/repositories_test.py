from src.models.sqlite.settings.connection import db_connection
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.repositories.owners_repository import OwnersRepository
import pytest

db_connection.connect()

@pytest.mark.skip(reason="DB integration test")
def test_list_all_pets():
    pets_repository = PetsRepository(db_connection)
    pets = pets_repository.list_all()
    assert len(pets) > 0

@pytest.mark.skip(reason="DB integration test")
def test_delete_pet():
    idd = 1
    pets_repository = PetsRepository(db_connection)
    pets_repository.delete(idd)

@pytest.mark.skip(reason="DB integration test")
def test_create_owner():
    first_name = "John"
    last_name = "Doe"
    age = 30
    pet_id = 1
    owners_repository = OwnersRepository(db_connection)
    owners_repository.create(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="DB integration test")
def test_get_owner_by_id():
    idd = 1
    owners_repository = OwnersRepository(db_connection)
    owners_repository.get_owner_by_id(idd)

