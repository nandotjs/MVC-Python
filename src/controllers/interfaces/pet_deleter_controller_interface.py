from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):
    @abstractmethod
    def delete(self, pet_id: int) -> None:
        pass 