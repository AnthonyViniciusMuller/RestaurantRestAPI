from typing import Dict
from src.core.use_cases.delete_restaurant import DeleteRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository


class DeleteRestaurant(DeleteRestaurant):
    
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository

    def by_id(self, id: int) -> Dict[bool, any]:
        
        if isinstance(id, int) == False:
            return {"success": False, "error": 'id is not a number'}
        if id < 0:
            return {"success": False, "error": 'id is negative'}

        success = self.restaurant_repository.delete_restaurant_by_id(id)

        if success:
            return {"success": True, "data": success}

        return {"success": False, "error": 'invalid id'}

