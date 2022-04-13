from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.tibiawiki.com.br/wiki/Calculadoras').content
#Objeto site recebendo o conteudo da requisição http do site
soup = BeautifulSoup(site,'html.parser')
#Objeto soup baixando do site o html

#print(soup.prettify())
#transforma toda a estrutura do html em string e exibe o html


texto = soup.find("span", class_="plainlinks")
print(texto.string)
#localiza o bloco e a classe e imprime o que esta nela

print(soup.title.string)
#imprime o texto do titulo do site

print(soup.find('admin'))