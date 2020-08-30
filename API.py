import requests
import json
from decimal import Decimal

#import secrets module for coinapi api-key
import secrets

#Use requests module for get request on coinapi
#Then create a json instance which I put in a dictionary
#Acces "rate" key and round on 2 decimals 
#Do this for ETH, LINK & LEND
url = 'https://rest.coinapi.io/v1/exchangerate/ETH/EUR'
headers = {'X-CoinAPI-Key' : secrets.MyApiKey}
response = requests.get(url, headers=headers)
dic = response.json()
rateEth = dic.get("rate")
rateEth = round(rateEth, 2)
#print("ETH  price is eur: ", API.rateEth)

url = 'https://rest.coinapi.io/v1/exchangerate/LINK/EUR'
headers = {'X-CoinAPI-Key' : secrets.MyApiKey}
response = requests.get(url, headers=headers)
dic = response.json()
rateLink = dic.get("rate")
rateLink = round(rateLink, 2)
#print("LINK price is eur: ", API.rateLink)

url = 'https://rest.coinapi.io/v1/exchangerate/LEND/EUR'
headers = {'X-CoinAPI-Key' : secrets.MyApiKey}
response = requests.get(url, headers=headers)
dic = response.json()
rateLend = dic.get("rate")
rateLend = round(rateLend, 2)
#print("LEND price is eur: ", API.rateLend)