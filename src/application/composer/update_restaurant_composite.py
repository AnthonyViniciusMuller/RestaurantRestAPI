from src.data.update_restaurant import UpdateRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository
from src.presenters.controllers.update_restaurant_controller import UpdateRestaurantController


def update_restaurant_composer() -> UpdateRestaurantController:

    repository = RestaurantRepository()
    use_case = UpdateRestaurant(repository)
    update_restaurant_route = UpdateRestaurantController(use_case)

    return update_restaurant_route
