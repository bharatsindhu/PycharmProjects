import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/forum/topic.php?id=1610'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup('<html><body><td class="second-column"><a class="user-name"><div class="post-content  tnb-bbcode-content"></div></a> </td></body</html>', "html.parser")
        for link in soup.findAll(True, {"class":["second-column", "user-name", "post-content  tnb-bbcode-content"]}):
           # final = str(link).replace('<code>','')
           # print(final)

            #fw = open('abc.txt', 'w')
            #fw.write(output)
            #fw.close()
            #for src in link.findAll('div', {'class':'post-content  tnb-bbcode-content'}):
               # print(src)
        page +=1

'''def get_details(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll():

        print(item_name)
'''




trade_spider(2)
