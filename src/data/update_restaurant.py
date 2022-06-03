from typing import Dict
from src.core.models.restaurant import Restaurant
from src.core.use_cases.update_restaurant import UpdateRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository


class UpdateRestaurant(UpdateRestaurant):
    
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository

    def by_id(self, id: int, restaurant: Restaurant) -> Dict[bool, any]:
        
        if isinstance(restaurant, Restaurant) == False:
            return {"success": False, "error": 'please post a restaurant'}

        success = self.restaurant_repository.update_restaurant(id, restaurant)

        if(success):
            return {"success": True, "data": True}

        return {"success": False, "error": 'invalid restaurant'}
