from abc import ABC, abstractmethod

class OwnerCreatorControllerInterface(ABC):
    @abstractmethod
    def create(self, owner_info: dict) -> dict:
        pass
