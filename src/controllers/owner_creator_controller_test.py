from src.controllers.owner_creator_controller import OwnerCreatorController

class MockOwnersRepository:
    def create(self, first_name: str, last_name: str, age: int, pet_id: int): # pylint: disable=unused-argument
        return 1  # Simula retornar o ID do owner criado

def test_owner_creator_controller():
    owner_creator_controller = OwnerCreatorController(MockOwnersRepository())
    owner_info = {"first_name": "John", "last_name": "Doe", "age": 30, "pet_id": 1}
    response = owner_creator_controller.create(owner_info)
    assert response["data"]["id"] == 1
    assert response["data"]["attributes"] == owner_info
