from src.core.models.mock_restaurant import create_mock_restaurant
from .restaurant_repository import RestaurantRepository


def test_insert():

    restaurant = create_mock_restaurant()

    id = RestaurantRepository.insert_restaurant(restaurant) 
    insert_restaurant = RestaurantRepository.get_restaurant_by_id(id)

    RestaurantRepository.delete_restaurant_by_id(id)
    
    assert insert_restaurant['name'] == restaurant.name
    assert insert_restaurant['postal_code'] == restaurant.postal_code
    assert sorted(insert_restaurant['categories']) == sorted([category.getEntity()['name'] for category in restaurant.categories])
    assert sorted(insert_restaurant['websites']) == sorted([website.getEntity()['url'] for website in restaurant.websites])

def test_update():

    restaurant = create_mock_restaurant()
    id = RestaurantRepository.insert_restaurant(restaurant) 

    new_restaurant = create_mock_restaurant()
    RestaurantRepository.update_restaurant(id = id, restaurant = new_restaurant)
    updated_restaurant = RestaurantRepository.get_restaurant_by_id(id)

    RestaurantRepository.delete_restaurant_by_id(id)

    assert updated_restaurant['name'] == new_restaurant.name
    assert updated_restaurant['postal_code'] == new_restaurant.postal_code
    assert sorted(updated_restaurant['categories']) == sorted([category.getEntity()['name'] for category in new_restaurant.categories])
    assert sorted(updated_restaurant['websites']) == sorted([website.getEntity()['url'] for website in new_restaurant.websites])

def test_get():

    restaurant = create_mock_restaurant()
    id = RestaurantRepository.insert_restaurant(restaurant) 

    restaurant = RestaurantRepository.get_restaurant_by_id(id)
    all_restaurant = RestaurantRepository.get_restaurants()

    RestaurantRepository.delete_restaurant_by_id(id)

    assert restaurant in all_restaurant
   

def teste_delete():

    restaurant = create_mock_restaurant()
    id = RestaurantRepository.insert_restaurant(restaurant) 

    try:
        restaurant = RestaurantRepository.get_restaurant_by_id(id)

        if(restaurant):
            RestaurantRepository.delete_restaurant_by_id(id)
            restaurant = RestaurantRepository.get_restaurant_by_id(id)
        else:
            raise Exception

    except:
        restaurant =  None

    assert restaurant != None
   