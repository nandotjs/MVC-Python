from typing import Dict
from src.models.sqlite.interfaces.owners_repository import OwnersRepositoryInterface
from src.models.sqlite.entities.owners import Owners
from src.controllers.interfaces.owner_finder_controller_interface import OwnerFinderControllerInterface

class OwnerFinderController(OwnerFinderControllerInterface):
    def __init__(self, owners_repository: OwnersRepositoryInterface):
        self.owners_repository = owners_repository

    def find(self, owner_id: int) -> Dict:
        owner = self.__find_owner_in_db(owner_id)
        return self.__format_response(owner)

    def __find_owner_in_db(self, owner_id: int) -> Owners:
        owner = self.owners_repository.get_owner_by_id(owner_id)
        if not owner:
            raise ValueError("Owner not found")
        return owner

    def __format_response(self, owner: Owners) -> dict:
        return {
            "data": {
                "type": "owner",
                "id": owner.id,
                "attributes": {
                    "first_name": owner.first_name,
                    "last_name": owner.last_name,
                    "age": owner.age,
                    "pet_id": owner.pet_id,
                    "pet": {
                        "name": owner.pet_name,
                        "type": owner.pet_type
                    } if owner.pet_name else None
                }
            }
        }

