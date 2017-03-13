import random
import urllib.request
import requests
from bs4 import BeautifulSoup


def download_web_image(url):
    name = random.randrange(1,100000)
    fullname = str(name) + '.jpg'
    urllib.request.urlretrieve(url, fullname)

def spider(max_pages):
    page =1
    while page <= max_pages:
        url = 'http://kimaya.in/occasion/bridal?p=' + str(page)
        sourcecode= requests.get(url)
        plaintext = sourcecode.text
        soup = BeautifulSoup(plaintext,"html.parser")
        for link in soup.findAll('img', {'class':'first_image'}):
            src = link.get('src')
            #title = link.get('title')
            #print(src)
            download_web_image(src)
            #print(title)
        page+=1

spider(15)