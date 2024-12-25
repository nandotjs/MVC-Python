from typing import Dict
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.controllers.interfaces.pet_deleter_controller_interface import PetDeleterControllerInterface

class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.pets_repository = pets_repository

    def delete(self, pet_id: int) -> Dict:
        try:
            self.pets_repository.delete(pet_id)
            return {
                "data": {
                    "type": "pet",
                    "message": "Pet deleted successfully"
                }
            }
        except Exception as error:
            return {
                "errors": [{
                    "status": "400",
                    "title": "Delete Failed",
                    "detail": str(error)
                }]
            } 