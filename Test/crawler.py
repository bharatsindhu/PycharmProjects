import  requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page =1
    while page <= max_pages:
        url = 'http://kimaya.in/occasion/bridal?p=' + str(page)
        sourcecode= requests.get(url)
        plaintext = sourcecode.text
        soup = BeautifulSoup(plaintext,"html.parser")
        for link in soup.findAll('a', {'class':'rspl-image'}):
            href = link.get('href')
            #title = link.get('title')
            print(href)
            get_single_item_data(href)
            #print(title)
        page+=1

def get_single_item_data(item_url):
    sourcecode = requests.get(item_url)
    plaintext = sourcecode.text
    soup = BeautifulSoup(plaintext,"html.parser")
    for item_name in soup.findAll('div',{'class':'price-box'}):
        for item_price in item_name.findAll('span', {'class': 'price'}):
            print(item_price.string)



spider(1)