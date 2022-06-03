from abc import ABC, abstractclassmethod
from typing import Dict
from src.core.models.restaurant import Restaurant


class AddRestaurant(ABC):

    @abstractclassmethod
    def add(self, restaurant: Restaurant) -> Dict[bool, any]:
        raise Exception("This method has not being implemented in the child Class")
