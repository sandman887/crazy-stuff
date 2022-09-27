import requests
from bs4 import BeautifulSoup
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

url = 'https://www.sfit.ac.in/'
reqs = requests.get(url,headers=headers)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []

while(True):
    try:
        for link in soup.find_all('a'):
                # print(link.get('href'))
            requests.get(url,headers=headers)
    except:
        continue
