from abc import ABC, abstractmethod
from typing import List
from src.core.models import Restaurant


class RestaurantInterface(ABC):

    @abstractmethod
    def insert_restaurant(cls, restaurant: Restaurant) -> int:
        raise Exception("This method has not being implemented in the child Class")

    def get_restaurants(cls) -> List[Restaurant]:
        raise Exception("This method has not being implemented in the child Class")
    
    @abstractmethod
    def get_restaurant_by_id(cls, id: int) -> Restaurant:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def delete_restaurant_by_id(cls, id: int) -> int:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def update_restaurant(cls, id: int, restaurant: Restaurant) -> bool:
        raise Exception("This method has not being implemented in the child Class")
        
