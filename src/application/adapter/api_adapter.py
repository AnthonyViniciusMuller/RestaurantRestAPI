from src.presenters.helpers.http_request import HttpRequest
from src.presenters.helpers.http_response import HttpResponse
from typing import Type
from src.application.interfaces.route import RouteInterface


def flask_adapter(request: any, route: Type[RouteInterface]) -> any:    
    
    params = request.args

    try:
        body = request.json
    except:
        body = request
        
    http_request = HttpRequest(
        header = request.headers, body = body, params = params
    )

    try:
        response = route.route(http_request)

    except Exception as exc:
        print(exc)
        return HttpResponse(
            code = 401, body = "Bad Resquest"
        )

    return response
