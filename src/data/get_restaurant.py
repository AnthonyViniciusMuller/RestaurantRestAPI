from typing import Dict
from src.core.use_cases.get_restaurant import GetRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository


class GetRestaurant(GetRestaurant):
    
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository

    def by_id(self, id: int) -> Dict[bool, any]:
        
        if isinstance(id, int) == False:
            return {"success": False, "error": 'id is not a number'}
        if id < 0:
            return {"success": False, "error": 'id is negative'}

        restaurant = self.restaurant_repository.get_restaurant_by_id(id)

        if restaurant:
            return {"success": True, "data": restaurant}

        return {"success": False, "error": 'invalid id'}

    def all(self) -> Dict[bool, any]:

        restaurants = self.restaurant_repository.get_restaurants()

        if len(restaurants) > 0:
            return {"success": True, "data": restaurants}

        return {"success": False, "error": 'invalid id'}
