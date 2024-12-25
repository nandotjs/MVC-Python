from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from src.models.sqlite.entities.pets import Pets

class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_all(self) -> List['Pets']:
        pass

    @abstractmethod
    def delete(self, pet_id: int) -> None:
        pass
