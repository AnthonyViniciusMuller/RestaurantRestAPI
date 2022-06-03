class WebSite:

    def __init__(self, url: str):
        self.url = url

    def getEntity(self):
        return {
            'url': self.url,
        }
    


