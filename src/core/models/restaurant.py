from typing import List
from src.core.models.website import WebSite
from src.core.models.category import Category


class Restaurant:

    def __init__(self, name: str, postal_code: str, address: str = None, country: str = None, province: str = None, city: str = None, latitude: float = 0, longitude: float = 0, categories: List[Category] = [], websites: List[WebSite] = []):
        self.name = name
        self.postal_code = postal_code
        self.address = address
        self.country = country
        self.province = province
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.categories = categories
        self.websites = websites

    def getEntity(self):
        return {
            'name': self.name,
            'postal_code': self.postal_code,
            'address': self.address,
            'country': self.country,
            'province': self.province,
            'city': self.city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'categories': self.categories,
            'websites': self.websites
        }

