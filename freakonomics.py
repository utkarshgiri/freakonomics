import time
import requests
from bs4 import BeautifulSoup, SoupStrainer
r = requests.get(url='https://freakonomics.com/archive/')
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table', 'radioarchive')
links = table.findAll('a')

for link in links[:3]:
    r = requests.get(url=link['href'])
    soup = BeautifulSoup(r.content, 'html.parser')	
    title = soup.find('title').get_text()
    link = str(soup).split('.mp3')
    l = 'https:' + link[0].split('https:')[-1] + '.mp3'
    doc = requests.get(l)
    with open(f'{title}.mp3', 'wb') as f:
            f.write(doc.content)
    time.sleep(2)
