from flask import Flask
from flask_restful import Api
from resources.PrevisaoResource import Previsao
from resources.CidadeResource import Cidade
app = Flask(__name__)
api = Api(app)

api.add_resource(Previsao, '/previsao_tempo/<string:cidadeID>')
api.add_resource(Cidade, '/cidade/<string:cidade>')

@app.route('/')
def index():  # put application's code here
    return 'Bem vindo a API - Previsão do Tempo Linx'

if __name__ == '__main__':
    app.run()
