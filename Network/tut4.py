import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls000049962/'
c1 = requests.get(url)
c2 = c1.text
c3 = BeautifulSoup(c2, "html.parser")
for L in c3.findAll('h3', {'class': 'lister-item-header'}):
    valor = L.span.get_text()
    texto1 = L.a.get_text()
    texto2 = L.a.get('href')
    print(valor + " - " + texto1 + " - " + texto2)
