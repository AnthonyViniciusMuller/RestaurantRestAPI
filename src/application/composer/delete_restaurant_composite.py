from src.data.delete_restaurant import DeleteRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository
from src.presenters.controllers.delete_restaurant_controller import DeleteRestaurantController


def delete_restaurant_composer() -> DeleteRestaurantController:

    repository = RestaurantRepository()
    use_case = DeleteRestaurant(repository)
    delete_restaurant_route = DeleteRestaurantController(use_case)

    return delete_restaurant_route
