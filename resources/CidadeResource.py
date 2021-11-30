import requests
from flask_restful import Resource, reqparse
from config import api_key

class Cidade(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('cidade_pais')
    argumentos.add_argument('coord')
    argumentos.add_argument('weather')
    argumentos.add_argument('main')
    argumentos.add_argument('wind')
    argumentos.add_argument('clouds')
    argumentos.add_argument('sys')
    argumentos.add_argument('id')
    argumentos.add_argument('timezone')
    argumentos.add_argument('name')


    def get(sef, cidade_pais):
        cidade = Cidade.find_cidade(cidade_pais)
        if cidade:
            return cidade
        return {'message': "Cidade não encontrada"}, 404

    def find_cidade(cidade_pais):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade_pais}&APPID={api_key}'
        response = requests.get(url).json()
        return response,200