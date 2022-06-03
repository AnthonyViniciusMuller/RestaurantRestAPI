from typing import List
from src.data.interfaces.restaurant_interface import RestaurantInterface
from src.persistent.MySQL.data_base.database_connection import DataBaseConnectionHandler
from src.core.models import Restaurant
from src.persistent.MySQL.repositories.category_repository import CategoryRepository
from src.persistent.MySQL.repositories.website_repository import WebSiteRepository


class RestaurantRepository(RestaurantInterface):

    @classmethod
    def insert_restaurant(cls, restaurant: Restaurant) -> int :
        restaurant_data = restaurant.getEntity()
        categories = restaurant_data['categories']
        websites   = restaurant_data['websites']

        del restaurant_data['categories']
        del restaurant_data['websites']

        columns = ['id']
        for column in restaurant_data:
            columns.append(f"`{column}`")

        values = ['DEFAULT']
        for column in restaurant_data:
            values.append(f"'{restaurant_data[column]}'")
        
        query = f"""
            INSERT INTO restaurant (
                {','.join(columns)}
            )
            Values (
                {','.join(values)}
            )
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                cursor = data_base.connection.cursor()
                cursor.execute(query)
                data_base.connection.commit()

                for category in categories: 
                    CategoryRepository.insert_category(restaurant_id = cursor.lastrowid, category = category)
                for website in websites: 
                    WebSiteRepository.insert_website(restaurant_id = cursor.lastrowid, website = website)
                
                return cursor.lastrowid

            except Exception as exception:
                print(exception)
                data_base.connection.rollback()

        return False

    @classmethod
    def get_restaurant_by_id(cls, id: int) -> Restaurant:
        
        query = f"""
            SELECT 
                restaurant.*, 
                GROUP_CONCAT(DISTINCT(category.name)) as categories, 
                GROUP_CONCAT(DISTINCT(website.url)) as websites
            FROM restaurant, category, website 
            WHERE 
                restaurant.id = category.restaurant_id AND 
                restaurant.id = website.restaurant_id AND
                restaurant.id = {id} 
            GROUP BY restaurant.id;
        """


        with DataBaseConnectionHandler() as data_base:
            try:
                cursor = data_base.connection.cursor(dictionary=True)
                cursor.execute(query)

                restaurant = cursor.fetchone()
                restaurant['categories'] = restaurant['categories'].split(',')
                restaurant['websites'] = restaurant['websites'].split(',')

                return restaurant
                    
            except Exception as exception:
                print(exception)

        return False

    @classmethod
    def get_restaurants(cls) -> List[Restaurant]:
        query = f"""
            SELECT restaurant.id
            FROM restaurant
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                cursor = data_base.connection.cursor(dictionary=True)
                cursor.execute(query)

                restaurants = []
                for restaurant_data in cursor.fetchall(): 
                    restaurants.append(cls.get_restaurant_by_id(restaurant_data['id'])) 

                return restaurants
                    
            except Exception as exception:
                print(exception)

        return []
    
    @classmethod
    def delete_restaurant_by_id(cls, id: int):
        query = f"""
            DELETE FROM restaurant
            WHERE id = {id} 
        """
        for category in CategoryRepository.get_categories_by_restaurant_id(id):
            CategoryRepository.delete_category_by_id(category['id'])

        for website in WebSiteRepository.get_websites_by_restaurant_id(id): 
            WebSiteRepository.delete_website_by_id(website['id'])   

        with DataBaseConnectionHandler() as data_base:
            try:
                cursor = data_base.connection.cursor(dictionary=True)
                cursor.execute(query)
                data_base.connection.commit()

                return True if cursor.rowcount > 0 else False
                    
            except Exception as exception:
                print(exception)

        return False

    @classmethod
    def update_restaurant(cls, id: int, restaurant: Restaurant):
        restaurant_data = restaurant.getEntity()
        categories = restaurant_data['categories']
        websites   = restaurant_data['websites']

        del restaurant_data['categories']
        del restaurant_data['websites']

        for category in CategoryRepository.get_categories_by_restaurant_id(id): 
            CategoryRepository.delete_category_by_id(category['id'])
        for website in WebSiteRepository.get_websites_by_restaurant_id(id): 
            WebSiteRepository.delete_website_by_id(website['id'])  

        columns = []
        for column in restaurant_data:
            columns.append(f"`{column}` = '{restaurant_data[column]}'")
        
        query = f"""
            UPDATE restaurant SET {','.join(columns)}
            WHERE id = {id}
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                cursor = data_base.connection.cursor()
                cursor.execute(query)
                data_base.connection.commit()

                for category in categories: 
                    CategoryRepository.insert_category(restaurant_id = id, category = category) 
                for website in websites: 
                    WebSiteRepository.insert_website(restaurant_id = id, website = website)
                
                return True if cursor.rowcount > 0 else False

            except Exception as exception:
                print(exception)
                data_base.connection.rollback()

        return False
