from src.presenters.helpers import HttpRequest, HttpResponse
from abc import ABC, abstractmethod
from typing import Type


class RouteInterface(ABC):

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise Exception("This method has not being implemented in the child Class")
