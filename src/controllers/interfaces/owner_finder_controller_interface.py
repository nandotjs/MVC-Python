from abc import ABC, abstractmethod

class OwnerFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, owner_id: int) -> dict:
        pass 