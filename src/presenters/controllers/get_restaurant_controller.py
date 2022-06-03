from src.application.interfaces.route import RouteInterface
from src.core.use_cases import GetRestaurant
from src.presenters.helpers.http_request import HttpRequest
from src.presenters.helpers.http_response import HttpResponse
from typing import Type


class GetRestaurantController(RouteInterface):

    def __init__(self, use_case: Type[GetRestaurant]):
        self.get_restaurant = use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        if http_request.params:

            params = http_request.params

            if "id" in params.keys() and isinstance(params['id'], int):
                response = self.get_restaurant.by_id(id = params['id'])
                
                if response['success'] == True:
                    return HttpResponse(code = 200, body = response["data"])

                return HttpResponse(code = 400, body = response["erro"])
        
        else:
            response = self.get_restaurant.all()
                
            if response['success'] == True:
                return HttpResponse(code = 200, body = response["data"])

            return HttpResponse(code = 400, body = response["erro"])

        return HttpResponse(code = 400, body = "Bad Request")
