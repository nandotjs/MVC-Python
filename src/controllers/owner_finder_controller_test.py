from src.controllers.owner_finder_controller import OwnerFinderController

class MockOwner:
    def __init__(self, id: int, first_name: str, last_name: str, age: int, pet_id: int): # pylint: disable=too-many-arguments 
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pet_id = pet_id

class MockOwnersRepository:
    def get_owner_by_id(self, owner_id: int): # pylint: disable=unused-argument
        return MockOwner(1, "John", "Doe", 30, 1)

def test_owner_finder_controller():
    owner_finder_controller = OwnerFinderController(MockOwnersRepository())
    response = owner_finder_controller.find(1)
    assert response["data"]["id"] == 1
    assert response["data"]["attributes"] == {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    }
