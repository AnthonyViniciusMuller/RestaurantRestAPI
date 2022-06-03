from abc import ABC, abstractmethod
from typing import List
from src.core.models import Category


class CategoryInterface(ABC):

    @abstractmethod
    def insert_category(cls, restaurant_id: int, category: Category) -> List[int]:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def get_category_by_id(cls, id: int) -> Category:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def get_categories_by_restaurant_id(cls, restaurant_id: int) -> List[Category]:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def delete_category_by_id(cls, id: int) -> int:
        raise Exception("This method has not being implemented in the child Class")
