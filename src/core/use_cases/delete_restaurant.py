from abc import ABC, abstractclassmethod
from typing import Dict


class DeleteRestaurant(ABC):

    @abstractclassmethod
    def by_id(self, id: int) -> Dict[bool, any]:
        raise Exception("This method has not being implemented in the child Class")
