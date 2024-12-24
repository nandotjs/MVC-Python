from src.controllers.pet_deleter_controller import PetDeleterController

class MockPetsRepository:
    def __init__(self):
        self.delete_called = False
        self.deleted_id = None

    def delete(self, pet_id: int) -> None:
        self.delete_called = True
        self.deleted_id = pet_id

    def list_all(self) -> list:
        return []

def test_pet_deleter_controller_success():
    mock_repository = MockPetsRepository()
    controller = PetDeleterController(mock_repository)
    
    response = controller.delete(1)
    
    assert mock_repository.delete_called
    assert mock_repository.deleted_id == 1
    assert response["data"]["type"] == "pet"
    assert response["data"]["message"] == "Pet deleted successfully"

def test_pet_deleter_controller_error():
    class FailingMockRepository(MockPetsRepository):
        def delete(self, pet_id: int) -> None: # pylint: disable=arguments-differ
            raise Exception("Database error")

    mock_repository = FailingMockRepository()
    controller = PetDeleterController(mock_repository)
    
    response = controller.delete(1)
    
    assert "errors" in response
    assert response["errors"][0]["status"] == "400"
    assert response["errors"][0]["title"] == "Delete Failed"
    assert response["errors"][0]["detail"] == "Database error" 