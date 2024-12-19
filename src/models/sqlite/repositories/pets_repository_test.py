from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import Pets
from src.models.sqlite.repositories.pets_repository import PetsRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Pets)],
                    [
                        Pets(id=1, name="Dog"), 
                        Pets(id=2, name="Cat")
                    ]
                )
            ]
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

def test_list_all_pets():
    mock_connection = MockConnection()
    pets_repository = PetsRepository(mock_connection)
    pets = pets_repository.list_all()
    assert pets[0].id == 1
    assert pets[1].name == "Cat"

def test_delete_pet_by_id():
    mock_connection = MockConnection()
    pets_repository = PetsRepository(mock_connection)
    pets_repository.delete(1)
    pets = pets_repository.list_all()
    assert len(pets) == 1
