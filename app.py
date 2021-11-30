from flask import Flask
from flask_restful import Api
from resources.CidadeResource import Cidade
app = Flask(__name__)
api = Api(app)

api.add_resource(Cidade, '/previsao_tempo/<string:cidade_pais>')



@app.route('/')
def index():  # put application's code here
    return 'Bem vindo a API - Previsão do Tempo Linx'

if __name__ == '__main__':
    app.run()
