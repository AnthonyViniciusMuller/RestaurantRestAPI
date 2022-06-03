from src.core.models.mock_restaurant import create_mock_restaurant
from src.data.add_restaurant import AddRestaurant
from src.data.get_restaurant import GetRestaurant
from .add_restaurant_controller import AddRestaurantController
from src.presenters.helpers.http_request import HttpRequest
from .get_restaurant_controller import GetRestaurantController
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository


def test_get_restaurant_controller():

    restaurant = create_mock_restaurant()

    id = RestaurantRepository.insert_restaurant(restaurant) 
    repository = RestaurantRepository()
    use_case = GetRestaurant(repository)
    get_restaurant_controller = GetRestaurantController(use_case)
    
    response = get_restaurant_controller.route(
        HttpRequest(params = {'id': id})
    )

    assert response.code <= 299
    assert response.code >= 200
    assert response.body['id'] == id

    RestaurantRepository.delete_restaurant_by_id(id)

def test_add_restaurant_controller():

    restaurant = create_mock_restaurant()
    
    add_restaurant_controller = AddRestaurantController(AddRestaurant(RestaurantRepository()))

    response = add_restaurant_controller.route(
        HttpRequest(body = {'restaurant': restaurant})
    )

    assert response.code <= 299
    assert response.code >= 200
    assert isinstance(response.body['id'], int)

    RestaurantRepository.delete_restaurant_by_id(response.body['id'])
