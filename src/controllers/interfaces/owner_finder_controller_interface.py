from abc import ABC, abstractmethod
from typing import Dict

class OwnerFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, owner_id: int) -> Dict:
        pass 