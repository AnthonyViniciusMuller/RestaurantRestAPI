from abc import ABC, abstractmethod
from typing import List
from src.core.models import WebSite


class WebSiteInterface(ABC):

    @abstractmethod
    def insert_website(cls, website: WebSite) -> List[int]:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def get_website_by_id(cls, id: int) -> WebSite:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def get_websites_by_restaurant_id(cls, websites: int) -> List[WebSite]:
        raise Exception("This method has not being implemented in the child Class")

    @abstractmethod
    def delete_website_by_id(cls, id: int) -> int:
        raise Exception("This method has not being implemented in the child Class")