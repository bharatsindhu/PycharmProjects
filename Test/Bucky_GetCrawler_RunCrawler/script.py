import  requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page =1
    while page <= max_pages:
        url = 'https://thenewboston.com/forum/topic.php?id=1610'
        sourcecode= requests.get(url)
        plaintext = sourcecode.text
        soup = BeautifulSoup(plaintext,"html.parser")
        for results in soup.find('code'):
            resultLine = str(results).replace('<br>', '\n').replace("\ufffd", '  ').replace('&l_t_;', '').replace(
                '</br>', '').replace('Â',' ')
            #resultcode=str(link).replace('<br>','\n')
            print(str(resultLine))
            fw=open('pythonBucky.txt','a+')
            fw.write(resultLine)
            fw.close()

            #for code in link.findAll('div', {'class': 'post-content tnb-bbcode-content'}):
                #print(code.string)


        #page+=1

spider(1)