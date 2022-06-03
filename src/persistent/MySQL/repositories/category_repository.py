from typing import List
from src.data.interfaces.category_interface import CategoryInterface
from src.persistent.MySQL.data_base.database_connection import DataBaseConnectionHandler
from src.core.models import Category


class CategoryRepository(CategoryInterface):

    @classmethod
    def insert_category(cls, restaurant_id: int, category: Category) -> int :
        category_data = category.getEntity()

        columns = ['id', 'restaurant_id']
        for column in category_data:
            columns.append(f"`{column}`")

        values = ['DEFAULT', f"'{restaurant_id}'"]
        for column in category_data:
            values.append(f"'{category_data[column]}'")
        
        query = f"""
            INSERT INTO category (
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
    def get_categories_by_restaurant_id(cls, restaurant_id: int) -> List[Category]:
        query = f"""
            SELECT * FROM category
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
    def delete_category_by_id(cls, id: int):
        query = f"""
            DELETE FROM category
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
