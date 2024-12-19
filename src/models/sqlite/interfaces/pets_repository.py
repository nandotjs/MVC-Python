from abc import ABC, abstractmethod
from src.models.sqlite.entities.pets import Pets

class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> list[Pets]:
        pass

    @abstractmethod
    def delete(self, pet_id: int) -> None:
        pass
