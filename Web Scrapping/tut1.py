import requests
from bs4 import BeautifulSoup
url = 'https://www.goibibo.com/hotels/hotels-in-goa-ct/'
# headers = {
#     'User-Agent' = ""
# }
response = requests.request("GET", url)
headers = {'User Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "}
data = BeautifulSoup(response.text, 'html.parser')

