from typing import List
from src.data.interfaces.website_interface import WebSiteInterface
from src.persistent.MySQL.data_base.database_connection import DataBaseConnectionHandler
from src.core.models import WebSite


class WebSiteRepository(WebSiteInterface):

    @classmethod
    def insert_website(cls, restaurant_id: int, website: WebSite) -> int :
        website_data = website.getEntity()

        columns = ['id', 'restaurant_id']
        for column in website_data:
            columns.append(f"`{column}`")

        values = ['DEFAULT', f"'{restaurant_id}'"]
        for column in website_data:
            values.append(f"'{website_data[column]}'")
        
        query = f"""
            INSERT INTO website (
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

                return cursor.lastrowid

            except Exception as exception:
                print(exception)
                data_base.connection.rollback()

        return False

    @classmethod
    def get_websites_by_restaurant_id(cls, restaurant_id: int) -> List[WebSite]:
        query = f"""
            SELECT * FROM website
            WHERE restaurant_id={restaurant_id}
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                cursor = data_base.connection.cursor(dictionary=True)
                cursor.execute(query)

                return cursor.fetchall()
                    
            except Exception as exception:
                print(exception)

        return []

    @classmethod
    def delete_website_by_id(cls, id: int):
        query = f"""
            DELETE FROM website
            WHERE id = {id} 
        """

        with DataBaseConnectionHandler() as data_base:
            try:
                cursor = data_base.connection.cursor(dictionary=True)
                cursor.execute(query)
                data_base.connection.commit()

                return cursor.rowcount
                    
            except Exception as exception:
                print(exception)

        return []
