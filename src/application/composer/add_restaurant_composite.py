from src.data.add_restaurant import AddRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository
from src.presenters.controllers.add_restaurant_controller import AddRestaurantController


def add_restaurant_composer() -> AddRestaurantController:

    repository = RestaurantRepository()
    use_case = AddRestaurant(repository)
    add_restaurant_route = AddRestaurantController(use_case)

    return add_restaurant_route
