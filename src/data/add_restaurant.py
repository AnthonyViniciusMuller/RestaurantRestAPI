from typing import Dict
from src.core.models.restaurant import Restaurant
from src.core.use_cases.add_restaurant import AddRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository


class AddRestaurant(AddRestaurant):
    
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository

    def add(self, restaurant: Restaurant) -> Dict[bool, any]:
        
        if isinstance(restaurant, Restaurant) == False:
            return {"success": False, "error": 'please post a restaurant'}

        id = self.restaurant_repository.insert_restaurant(restaurant)

        if(id):
            return {"success": True, "data": self.restaurant_repository.get_restaurant_by_id(id)}

        return {"success": False, "error": 'invalid restaurant'}
