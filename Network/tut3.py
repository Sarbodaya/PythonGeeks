import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Apple_Inc.'
c1 = requests.get(url)
c2 = c1.text
c3 = BeautifulSoup(c2, "html.parser")
for i in c3.find_all(['a']):
    print(i.text)
