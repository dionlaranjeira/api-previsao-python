from datetime import datetime
import requests
from config import api_key

#Definir os dias da semana
def retornaDiaSemana(dtTXT):
    seg = 1
    ter = 2
    qua = 3
    qui = 4
    sex = 5
    sab = 6
    dt = datetime.fromisoformat(dtTXT)
    diaSemana = dt.isoweekday()
    if(diaSemana == seg):
        return "SEG"
    elif(diaSemana == ter):
        return "TER"
    elif (diaSemana == qua):
        return "QUA"
    elif (diaSemana == qui):
        return "QUI"
    elif (diaSemana == sex):
        return "SEX"
    elif (diaSemana == sab):
        return "SAB"
    else:
        return "DOM"


def retornaHoje():
    hoje = (datetime.today())

    minute = ''
    if(hoje.minute <10):
        minute = "0"+str(hoje.minute)
    else:
        minute = str(hoje.minute)

    hojeFormatado = str(hoje.hour) + ":"+ minute +"h - " + str(hoje.day) + " de " +retornaMes()
    return hojeFormatado


def retornaMes():
    hoje = (datetime.today())
    mesAtual = hoje.month

    if(mesAtual == 1):
        return "Janeiro"
    elif(mesAtual == 2):
        return "Fevereiro"
    elif (mesAtual == 3):
        return "Março"
    elif (mesAtual == 4):
        return "Abril"
    elif (mesAtual == 5):
        return "Maio"
    elif (mesAtual == 6):
        return "Junho"
    elif (mesAtual == 7):
        return "Julho"
    elif (mesAtual == 8):
        return "Agosto"
    elif (mesAtual == 9):
        return "Setembro"
    elif (mesAtual == 10):
        return "Outubro"
    elif (mesAtual == 11):
        return "Novembro"
    elif (mesAtual == 12):
        return "Dezembro"


def convert_az_to_bearing(a):
    """Pega o azimute, que deve ser de 0-360 graus, e retorna uma string N / E / S / W.
     O norte é 0 graus."""
    directionWind = ""
    if a > 360 or a < 0 or not a:
        directionWind = ""
    elif a >= 348.75 or a < 11.25:
        directionWind = "Norte"
    elif a >= 11.25 and a < 33.75:
        directionWind = "Norte-Nordeste"
    elif a >= 33.75 and a < 56.25:
        directionWind = "Nordeste"
    elif a >= 56.25 and a < 78.75:
        directionWind = "Nordeste"
    elif a >= 78.75 and a < 101.25:
        directionWind = "Leste"
    elif a >= 101.25 and a < 123.75:
        directionWind = "Leste-Sudeste"
    elif a >= 123.75 and a < 146.25:
        directionWind = "Sudeste"
    elif a >= 146.25 and a < 168.75:
        directionWind = "Sul-Sudeste"
    elif a >= 168.75 and a < 191.25:
        directionWind = "Sul"
    elif a >= 191.25 and a < 213.75:
        directionWind = "Sudoeste"
    elif a >= 213.75 and a < 236.25:
        directionWind = "Sudoeste"
    elif a >= 236.25 and a < 258.75:
        directionWind = "Oeste-Sudoeste"
    elif a >= 258.75 and a < 281.25:
        directionWind = "Oeste"
    elif a >= 281.25 and a < 303.75:
        directionWind = "Oeste-Noroeste"
    elif a >= 303.75 and a < 326.25:
        directionWind = "Noroeste"
    elif a >= 326.25 and a < 348.75:
        directionWind = "Noroeste"
    else:
        directionWind = ""

    return directionWind + " (" + str(a) + ")"


def convert_wind_for_human(speed_wind):
    wind_description = ''
    if(speed_wind < 0.3):
        wind_description = "Calmo"
    elif(speed_wind <= 1.5):
        wind_description = "Aragem"
    elif (speed_wind <= 3.3):
        wind_description = "Brisa leve"
    elif (speed_wind <= 5.4):
        wind_description = "Brisa fraca"
    elif (speed_wind <= 7.9):
        wind_description = "Brisa moderada"
    elif (speed_wind <= 10.7):
        wind_description = "Brisa forte"
    elif (speed_wind <= 13.8):
        wind_description = "Vento fresco"
    elif (speed_wind <= 17.1):
        wind_description = "Vento forte"
    elif (speed_wind <= 20.7):
        wind_description = "Ventania"
    elif (speed_wind <= 24.4):
        wind_description = "Ventania forte"
    elif (speed_wind <= 28.4):
        wind_description = "Tempestade"
    elif (speed_wind <= 32.6):
        wind_description = "Tempestada violenta"
    elif (speed_wind > 32.6):
        wind_description = "Furacão"

    return wind_description


def convert_ms_km(wind_speed):
    km = wind_speed * 3.6

    return round(km,2)


def convert_kelvin_celsius(temp):
    celsius = temp - 273.15
    return round(celsius,2)


def convert_unix_hour(unix):
    hora = datetime.fromtimestamp(unix).strftime('%H:%M')
    return hora


def find_forecasts(cidadeID):

    forecast = []

    semana = find_index_week(cidadeID)

    previsao = {'day':'previsao'}
    url = f'http://api.openweathermap.org/data/2.5/forecast?id={cidadeID}&appid={api_key}&lang=pt_br'
    response = requests.get(url).json()
    lista = response['list']

    for linha in semana:
        day = linha['day']
        index = linha['index']

        description = lista[index]['weather'][0]['description']

        # RETORNANDO O ICON
        icon = lista[index]['weather'][0]['icon']

        #RETORNANDO MAIN_TODAY
        temp = lista[index]['main']['temp']
        tempCelsius = str(convert_kelvin_celsius(temp)) + "ºC"

        #RETORNANDO PRESSAO ATMOSFERICA
        pressure = lista[index]['main']['pressure']
        pressure = str(pressure) + " hpa"

        #RETORNANDO A HUMIDADE
        humidity = lista[index]['main']['humidity']
        humidity = str(humidity) +"%"

        # RETORNANDO CLOUDS

        clouds = lista[index]['clouds']['all']
        clouds = str(clouds)+"%"

        # RETORNNDO GEO CODE
        lat = response['city']['coord']['lat']
        lon = response['city']['coord']['lon']
        coords = str(lat) + ", " + str(lon)

        #RETORNANDO STATUS WIND
        wind_deeg = lista[index]['wind']['deg']
        wind_speed = lista[index]['wind']['speed']
        wind_text = convert_wind_for_human(wind_speed)
        wind_status = wind_text +", " + str(convert_ms_km(wind_speed)) + " km/h, " + convert_az_to_bearing(wind_deeg)

        wind_speed = str(convert_ms_km(wind_speed)) + " km/h"

        #RETORNANDO SUNRISE
        sunrise = response['city']['sunrise']
        sunrise = convert_unix_hour(sunrise)

        # RETORNANDO SUNSET
        sunset = response['city']['sunset']
        sunset = convert_unix_hour(sunset)

        # RETORNADO data
        data = lista[index]['dt_txt']
        date = retorna_dia_mes(data)

        novaPrevisaoHoje = {
                               "temp": tempCelsius,
                               "wind":wind_status,
                               "cloudiness": wind_text,
                               "pressure": pressure,
                               "humidity":humidity,
                                "sunrise":sunrise,
                                "sunset":sunset,
                                "icon":icon,
                                "date":date,
                                "clouds": clouds,
                                "wind_speed":wind_speed,
                                "coords": coords


        }

        newForecast = {
            day: novaPrevisaoHoje,
        }

        forecast.append(newForecast)

    return forecast


def retorna_dia_mes(dt_txt):
    dt = datetime.fromisoformat(dt_txt)

    mes = dt.month
    dia = str(dt.day)
    nomeMes = str(retornaMes_by_int(mes))

    return dia+ " de "+ nomeMes


    # minute = ''
    # if(hoje.minute <10):
    #     minute = "0"+str(hoje.minute)
    # else:
    #     minute = str(hoje.minute)
    #
    # hojeFormatado = str(hoje.hour) + ":"+ minute +"h - " + str(hoje.day) + " de " +retornaMes()
    # return hojeFormatado


def retornaMes_by_int(mes):

    if(mes == 1):
        return "Janeiro"
    elif(mes == 2):
        return "Fevereiro"
    elif (mes == 3):
        return "Março"
    elif (mes == 4):
        return "Abril"
    elif (mes == 5):
        return "Maio"
    elif (mes == 6):
        return "Junho"
    elif (mes == 7):
        return "Julho"
    elif (mes == 8):
        return "Agosto"
    elif (mes == 9):
        return "Setembro"
    elif (mes == 10):
        return "Outubro"
    elif (mes == 11):
        return "Novembro"
    elif (mes == 12):
        return "Dezembro"

def find_index_week(cidadeID):
    semana = []
    diaAtual=""
    url = f'http://api.openweathermap.org/data/2.5/forecast?id={cidadeID}&appid={api_key}&lang=pt_br'
    response = requests.get(url).json()
    lista = response['list']

    i = 0
    for linha in lista:
        diaObtido = retornaDiaSemana(lista[i]['dt_txt'])

        if diaObtido != diaAtual:
            diaAtual = diaObtido
            dia = {'day':diaAtual,
             'index':i}
            semana.append(dia)

        i = i + 1
    return semana







