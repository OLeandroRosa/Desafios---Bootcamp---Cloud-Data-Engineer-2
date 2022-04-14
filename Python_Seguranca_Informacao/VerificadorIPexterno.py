import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url) #abre o site e instancia a função

dados = json.load(resposta)# transforma os dados da pagina que são Json em dicionário
ip = dados ['ip']
org = dados ['org']
cid = dados ['city']
pais = dados ['country']
regiao = dados['region']

print('Detalhes do IP externo \n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.:{0}'.format(org,regiao,pais,cid,ip))