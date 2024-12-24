from src.controllers.pet_lister_controller import PetListerController

class MockPet:
    def __init__(self, id: int, name: str, age: int, owner_id: int):
        self.id = id
        self.name = name
        self.age = age
        self.owner_id = owner_id

class MockPetsRepository:
    def list_all(self):
        return [
            MockPet(1, "Rex", 3, 1),
            MockPet(2, "Fluffy", 2, 2)
        ]

def test_pet_lister_controller():
    pet_lister_controller = PetListerController(MockPetsRepository())
    response = pet_lister_controller.list()
    
    assert len(response) == 2
    assert response[0]["type"] == "pet"
    assert response[0]["id"] == 1
    assert response[0]["name"] == "Rex"
    assert response[0]["age"] == 3
    assert response[0]["owner_id"] == 1
    
    assert response[1]["type"] == "pet"
    assert response[1]["id"] == 2
    assert response[1]["name"] == "Fluffy"
    assert response[1]["age"] == 2
    assert response[1]["owner_id"] == 2 