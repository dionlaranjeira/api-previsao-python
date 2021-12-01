from flask_restful import Resource, reqparse
import json
jsonCitys = open('city.list.json')
citys = json.load(jsonCitys)

class Cidade(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('id')
    argumentos.add_argument('name')
    argumentos.add_argument('country')

    def get(sef, cidade):
        response = Cidade.find_cidade(cidade)
        if len(response)>0:
            return response, 200
        return {'message': "nenhuma cidade encontrada"}, 404

    def find_cidade(cidade):
        listaCidades = []
        for city in citys:
            if (city['name'].lower().find(cidade) >= 0):
                novaCidade = {
                    "id": (city['id']),
                    "name": (city['name']),
                    "country": city['country']}
                listaCidades.append(novaCidade)
        return listaCidades