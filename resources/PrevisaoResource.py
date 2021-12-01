import requests
from flask_restful import Resource
from config import api_key
class Previsao(Resource):

    def get(sef, cidadeID):
        previsao = Previsao.find_previsao(cidadeID)
        if previsao:
            return previsao
        return {'message': "Previsão não disponível"}, 404

    def find_previsao(cidadeID):
        url = f'http://api.openweathermap.org/data/2.5/forecast?id={cidadeID}&appid={api_key}&lang=pt_br'
        response = requests.get(url).json()
        return response