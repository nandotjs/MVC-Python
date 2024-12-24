from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import Pets

class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.pets_repository = pets_repository

    def list(self) -> dict:
        pets = self.__get_pets_from_db()
        return self.__format_response(pets)

    def __get_pets_from_db(self) -> list[Pets]:
        return self.pets_repository.list_all()

    def __format_response(self, pets: list[Pets]) -> dict:
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
    
    