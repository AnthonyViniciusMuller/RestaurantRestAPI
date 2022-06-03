from typing import Type
from src.application.interfaces.route import RouteInterface
from src.core.models.category import Category
from src.core.models.restaurant import Restaurant
from src.core.models.website import WebSite
from src.core.use_cases.add_restaurant import AddRestaurant
from src.presenters.helpers.http_request import HttpRequest
from src.presenters.helpers.http_response import HttpResponse


class AddRestaurantController(RouteInterface):

    def __init__(self, use_case: Type[AddRestaurant]):
        self.add_restaurant = use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        if http_request.body:

            body = http_request.body
            
            if ('name' and 'postal_code' in body.keys()):

                if("categories" in body.keys() and len(body["categories"]) > 0):
                    categories = body["categories"] 
                else:
                    categories = [],

                if("websites" in body.keys() and len(body["websites"]) > 0):
                    websites = body["websites"] 
                else:
                    websites = [],
                
                restaurant = Restaurant(
                    name = body["name"],
                    postal_code = body["postal_code"],
                    address = body["address"] if "address" in body.keys() else "",
                    country = body["country"] if "country" in body.keys() else "",
                    province = body["province"] if "province" in body.keys() else "",
                    city = body["city"] if "city" in body.keys() else "",
                    latitude = body["latitude"] if "latitude" in body.keys() else 0,
                    longitude = body["longitude"] if "longitude" in body.keys() else 0,
                    categories = [Category(name = category) for category in categories],
                    websites = [WebSite(url = website) for website in websites]
                )

                response = self.add_restaurant.add(restaurant)
                
                if response['success'] == True:
                    return HttpResponse(code = 200, body = response["data"])

                return HttpResponse(code = 400, body = response["erro"])

            return HttpResponse(code = 404, body = 'Bad Request')

        return HttpResponse(code = 402, body = "Bad Request")
