from typing import Dict


class HttpResponse:

    def __init__(self, code: int, body: any):
        self.code = code
        self.body = body

