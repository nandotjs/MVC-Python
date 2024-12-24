from abc import ABC, abstractmethod
from typing import List, Dict

class PetListerControllerInterface(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        pass 