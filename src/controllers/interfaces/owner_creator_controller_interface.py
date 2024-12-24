from abc import ABC, abstractmethod
from typing import Dict

class OwnerCreatorControllerInterface(ABC):
    @abstractmethod
    def create(self, owner_info: dict) -> Dict:
        pass
