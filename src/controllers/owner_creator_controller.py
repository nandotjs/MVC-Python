from src.models.sqlite.interfaces.owners_repository import OwnersRepositoryInterface
from src.controllers.interfaces.owner_creator_controller_interface import OwnerCreatorControllerInterface
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
import re

class OwnerCreatorController(OwnerCreatorControllerInterface):
    def __init__(self, owners_repository: OwnersRepositoryInterface):
        self.owners_repository = owners_repository

    def create(self, owner_info: dict) -> dict:
        first_name = owner_info["first_name"]
        last_name = owner_info["last_name"]
        age = owner_info["age"]
        pet_id = owner_info["pet_id"]

        self.__validate_names(first_name, last_name)
        owner_id = self.__insert_owner(first_name, last_name, age, pet_id)
        return self.__format_response(owner_info, owner_id)

    def __validate_names(self, first_name: str, last_name: str) -> None:
        non_valid_caracters = re.compile(r'[^a-zA-Z]')
        if non_valid_caracters.search(first_name) or non_valid_caracters.search(last_name):
            raise HttpUnprocessableEntityError("First name and last name must contain only letters")

    def __insert_owner(self, first_name: str, last_name: str, age: int, pet_id: int) -> int:
        return self.owners_repository.create(first_name, last_name, age, pet_id)

    def __format_response(self, owner_info: dict, owner_id: int) -> dict:
        return {
            "data": {
                "type": "owner",
                "id": owner_id,
                "attributes": owner_info
            }
        }
