import re
import fire
import time
import difflib
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)

r = requests.get(url='https://freakonomics.com/archive/')
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table', 'radioarchive')
links = table.findAll('a')
episode_num = table.find_all('td', text=re.compile(r'^[\n\s]*\d+[\n\s]*$'))
episode_name = [x.text for x in table.find_all('a')]

def download_link(link):
    r = requests.get(url=link['href'])
    soup = BeautifulSoup(r.content, 'html.parser')	
    title = soup.find('title').get_text()
    link = str(soup).split('.mp3')
    l = 'https:' + link[0].split('https:')[-1] + '.mp3'
    doc = requests.get(l)
    with open(f'{title}.mp3', 'wb') as f:
        f.write(doc.content)


def all():
    for link in links:
        download_link(link)
        time.sleep(2)

def by_episode_number(num):
    num = int(num)
    index = numpy.where(numpy.array(episode_num) == num)
    download_link(links[index])


def by_episode_name(name):
    logging.debug('Searching by episode name')
    index = episode_name.index(difflib.get_close_matches(name, episode_name, n=3, cutoff=0.0)[0])
    logging.info(f'Downloading Episode : {episode_name[index]}')
    download_link(links[index])

if __name__ == "__main__":
    fire.Fire()
