from .restaurant import Restaurant
from .category import Category
from .website import WebSite
from faker import Faker as Mocker


def create_mock_restaurant():
    mocker = Mocker()

    return Restaurant(
        name = mocker.name(),
        postal_code = mocker.word(),
        address = mocker.word(),
        country = mocker.word(),
        province = mocker.word(),
        city = mocker.word(),
        latitude = 323.231,
        longitude = 223.455,
        categories = [
            Category(name = mocker.word()),
            Category(name = mocker.word()),
            Category(name = mocker.word())
        ],
        websites = [
            WebSite(url = f"www.{mocker.word()}.com"),
            WebSite(url = f"www.{mocker.word()}.com"),
            WebSite(url = f"www.{mocker.word()}.com")
        ]
    )