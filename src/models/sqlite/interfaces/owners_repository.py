from abc import ABC, abstractmethod
from src.models.sqlite.entities.owners import Owners

class OwnersRepositoryInterface(ABC):
    @abstractmethod
    def create(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

    @abstractmethod
    def get_owner_by_id(self, id: int) -> Owners:
        pass
