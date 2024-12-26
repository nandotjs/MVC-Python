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
    controller = PetListerController(MockPetsRepository())
    response = controller.list()
    
    assert len(response) == 2
    assert response[0]["type"] == "pet"
    assert response[0]["id"] == 1
    assert response[0]["name"] == "Rex"

def test_pet_lister_empty_list():
    class EmptyMockRepository:
        def list_all(self):
            return []
    
    controller = PetListerController(EmptyMockRepository())
    response = controller.list()
    
    assert len(response) == 0 