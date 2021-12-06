from flask_restful import Resource, reqparse
import json
jsonCitys = open('city.list.json')
citys = json.load(jsonCitys)

class Cidade(Resource):

    def get(sef, cidade):
        response = Cidade.find_cidade(cidade)
        if len(response)>0:
            return response, 200
        return {'message': "Nenhuma cidade encontrada"}, 404

    def find_cidade(nome_cidade):
        listaCidades = []
        for city in citys:
            if (city['name'].lower().find(nome_cidade.lower()) >= 0):
                novaCidade = {
                    "id": (city['id']),
                    "name": (city['name']),
                    "country": city['country']}
                listaCidades.append(novaCidade)
        return listaCidades