from src.models.sqlite.interfaces.owners_repository import OwnersRepositoryInterface

class OwnerCreatorController:
    def __init__(self, owners_repository: OwnersRepositoryInterface):
        self.owners_repository = owners_repository

    def create(self, first_name: str, last_name: str, age: int, pet_id: int):
        self.owners_repository.create(first_name, last_name, age, pet_id)
