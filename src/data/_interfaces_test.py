from src.core.models.mock_restaurant import create_mock_restaurant
from .add_restaurant import AddRestaurant
from src.persistent.MySQL.repositories.restaurant_repository import RestaurantRepository
from .get_restaurant import GetRestaurant


def test_add_restaurant():
    add_restaurant = AddRestaurant(RestaurantRepository())
    restaurant_repository = RestaurantRepository()

    restaurant = create_mock_restaurant()

    id = RestaurantRepository.insert_restaurant(restaurant = restaurant) 
    repository_restaurant = restaurant_repository.get_restaurant_by_id(id)
    del repository_restaurant['id'] 

    use_case_restaurant = add_restaurant.add(restaurant)   
    del use_case_restaurant['data']['id'] 

    RestaurantRepository.delete_restaurant_by_id(id)

    assert use_case_restaurant['data'] == repository_restaurant
    assert use_case_restaurant['success'] == True

def test_get_restaurant():
    get_restaurant = GetRestaurant(RestaurantRepository())
    restaurant_repository = RestaurantRepository()

    restaurant = create_mock_restaurant()

    id = RestaurantRepository.insert_restaurant(restaurant) 

    use_case_restaurant = get_restaurant.by_id(id)    
    repository_restaurant = restaurant_repository.get_restaurant_by_id(id)

    RestaurantRepository.delete_restaurant_by_id(id)

    assert use_case_restaurant['data'] == repository_restaurant
    assert use_case_restaurant['success'] == True