from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.controllers.interfaces.pet_lister_controller_interface import PetListerControllerInterface
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from src.models.sqlite.entities.pets import Pets


class PetListerController(PetListerControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.pets_repository = pets_repository

    def list(self) -> List[dict]:
        pets = self.__get_pets_from_db()
        return self.__format_response(pets)

    def __get_pets_from_db(self) -> List['Pets']:
        return self.pets_repository.list_all()

    def __format_response(self, pets: List['Pets']) -> List[dict]:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({
                "type": "pet",
                "id": pet.id,
                "name": pet.name,
                "age": pet.age,
                "owner_id": pet.owner_id
            })
        return formatted_pets
    
    