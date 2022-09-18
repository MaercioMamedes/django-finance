from .models import Asset
from django.http import Http404
import yfinance as yf
from time import sleep
from datetime import datetime
import json


def factor_asset(args):
    data_b3 = yf.Ticker(args).info

    if 'longName' in data_b3.keys():
        name = data_b3['longName']
        ticker = args
        price = data_b3['currentPrice']
        url_image = data_b3['logo_url']

        return Asset.objects.create(name=name, ticker=ticker, price=price, url_image=url_image)
    else:
        return None


def download_br():
    with open('b3.json','r') as file_json:
        text = file_json.read()
        data = json.loads(text)

    contador = 0
    inicio = ''
    fim = ''

    for element in data.keys():
        contador += 1
        inicio = datetime.now()
        factor_asset(element+'.SA')
        fim = datetime.now()
        print(f'contagem {contador} ----- Papel {element} ------ tempo: {fim-inicio}')
        sleep(2)


def teste():
    with open('b3.json','r') as file_json:
        text = file_json.read()
        data = json.loads(text)

    for x in data.keys():
        print(x+'.SA')