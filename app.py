from flask import Flask

#dependencias
import requests

app = Flask(__name__)

api_key = '2a149d289a2eeb9716e157bd1448dfb3'

def openWeather(cidade, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&APPID={api_key}'
    response = requests.get(url).json()
    print(response)

@app.route('/')
def index():  # put application's code here
    openWeather("Boa Vista,BR",api_key)
    return 'Bem vindo a API - Previsão do Tempo Linx'

if __name__ == '__main__':
    app.run()
