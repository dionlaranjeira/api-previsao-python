class CidadeModel:
    def __init__(self, cidade_pais, coord, weather, main, wind, clouds, sys, id, timezone, name):
        self.cidade_pais = cidade_pais
        self.coord = coord
        self.weather = weather
        self.main = main
        self.clouds = clouds
        self.sys = sys
        self.id = id
        self.timezone = timezone
        self.name = name

    def json(self):
        return{
            'cidade_pais':self.cidade_pais,
            'coord':self.coord,
            'weather': self.weather,
            'main': self.main,
            'clouds': self.clouds,
            'sys': self.sys,
            'id': self.id,
            'timezone': self.timezone,
            'name': self.name
        }