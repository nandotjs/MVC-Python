from src.models.sqlite.settings.connection import db_connection
from src.models.sqlite.repositories.pets_repository import PetsRepository

db_connection.connect()

def test_list_all_pets():
    pets_repository = PetsRepository(db_connection)
    pets = pets_repository.list_all()
    assert len(pets) > 0

def test_delete_pet():
    pets_repository = PetsRepository(db_connection)
    pets_repository.delete(1)
    pets = pets_repository.list_all()
    assert len(pets) == 4
