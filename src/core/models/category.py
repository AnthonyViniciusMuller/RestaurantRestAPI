class Category:

    def __init__(self, name: str):
        self.name = name

    def getEntity(self):
        return {
            'name': self.name,
        }
    
    
