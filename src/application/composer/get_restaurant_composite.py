from src.data.get_restaurant import GetRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository
from src.presenters.controllers.get_restaurant_controller import GetRestaurantController


def get_restaurant_composer() -> GetRestaurantController:

    repository = RestaurantRepository()
    use_case = GetRestaurant(repository)
    get_restaurant_route = GetRestaurantController(use_case)

    return get_restaurant_route
