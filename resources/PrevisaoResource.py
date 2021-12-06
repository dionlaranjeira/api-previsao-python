import requests
from flask_restful import Resource
from config import api_key
from PrevisaoUtil import find_forecasts


class Previsao(Resource):

    def get(sef, cidadeID):
        previsao = find_forecasts(cidadeID)
        if previsao:
            return previsao
        return {'message': "Previsão não disponível"}, 404

