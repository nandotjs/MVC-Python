from src.controllers.owner_creator_controller import OwnerCreatorController
import pytest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class MockOwnersRepository:
    def create(self, first_name: str, last_name: str, age: int, pet_id: int): # pylint: disable=unused-argument
        return 1  # Simula retornar o ID do owner criado

def test_owner_creator_controller():
    owner_creator_controller = OwnerCreatorController(MockOwnersRepository())
    owner_info = {"first_name": "John", "last_name": "Doe", "age": 30, "pet_id": 1}
    response = owner_creator_controller.create(owner_info)
    assert response["data"]["id"] == 1
    assert response["data"]["attributes"] == owner_info

def test_owner_creator_invalid_name():
    owner_creator_controller = OwnerCreatorController(MockOwnersRepository())
    owner_info = {"first_name": "John123", "last_name": "Doe", "age": 30, "pet_id": 1}
    
    with pytest.raises(HttpUnprocessableEntityError, match="First name and last name must contain only letters"):
        owner_creator_controller.create(owner_info)

def test_owner_creator_repository_error():
    class FailingMockRepository(MockOwnersRepository):
        def create(self, first_name: str, last_name: str, age: int, pet_id: int):
            raise Exception("Database error")
    
    owner_creator_controller = OwnerCreatorController(FailingMockRepository())
    owner_info = {"first_name": "John", "last_name": "Doe", "age": 30, "pet_id": 1}
    
    with pytest.raises(Exception, match="Database error"):
        owner_creator_controller.create(owner_info)
