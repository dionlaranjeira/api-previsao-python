class CidadeModel:
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country

    def json(self):
        return{
            'id':self.id,
            'name':self.name,
            'country': self.country,
        }