'''magicnumber = 50

for n in range(101):
    if n % 4 == 0 :
        print(n,)




numbertaken = [2,4,6,8,16,17]

print("here are numbers taken")

for n in range(5,20):
    if n in numbertaken:
        break
    print(n)




def abhi():
    print("functions are cool")

def bitcoin_to_usd(btc):
    amount = btc*527
    print(amount)

abhi()
bitcoin_to_usd(3.85)
bitcoin_to_usd(13)



def allowed_dating_age(my_age):
    girls_age = my_age/2 +7
    return girls_age

abhi_limit = allowed_dating_age(27)
print("abhi can date",abhi_limit,"or older")




def get_gender(sex='unknown'):
    if sex is 'm':
        sex = "male"
    elif sex is 'f':
        sex = "female"
    print(sex)


get_gender('m')
get_gender('f')
get_gender()


a = 1234  #varibale defined ouside function
def corn():
    print(a)

def fudge():
    print(a)
corn()
fudge()




# default parameters
def dumb_sentence(name='abhi', action='love', person='minal'):
    print(name, action, person)


dumb_sentence()
dumb_sentence("minal", "love", "abhi")
dumb_sentence(action='too much love' , person='bae')




# function takes any amount of arguments

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)


add_numbers(3)
add_numbers(3 + 23)
add_numbers(3 + 4 + 5)




def health_cal(age,apples_ate,cig_smoke):
    answer = (100-age) + (apples_ate*3.5) - (cig_smoke*2)
    print(answer)

abhi_data = [27,20,5]
health_cal(abhi_data[0],abhi_data[1], abhi_data[2])
health_cal(*abhi_data) # unpack the arguments



shopping = {'milk','veggie','beer','shampoo', 'beer '}   #set

print(shopping)

if 'milk' in shopping:
    print("you already have milk abhi")
else:
    print("oh yeah , you need milk ")



classmates = {'abhi': ' cool but awesome', 'xyz': ' cool but bad', 'abc': ' good'}

#print(classmates)
#print(classmates['abhi'])


for i,v in classmates.items():
    print(i + v )



# MODULES

import abhi
import random
abhi.fish()
x = random.randrange(1,10)
print(x)

'''
'''
import random
import urllib.request


def download_web_imagae(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


download_web_imagae('http://www.freeusandworldmaps.com/images/Flags_Images/India-inflag.jpg')
'''
# how to read and write file
'''
fw = open('sample.txt','w')
fw.write('writing my stuff in my text file\n')
fw.write('this is second line \n')
fw.close()

fr = open('sample.txt','r')
text = fr.read()

print(text)
fr.close()

'''
'''

#downloading file from web

from urllib import request

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=0&b=16&c=2017&d=1&e=16&f=2017&g=d&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)


'''
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://hptdc.nic.in/ohrs/PublicPages/PubHome.aspx'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for links in soup.findAll('a', {'target':'_blank'}):
            href = links.get('href')
            title = links.string

            #print(href)
            #print(title)
        get_single_item_data(href)
        page += 1




def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    # if you want to gather information from that page
    for item_name in soup.findAll('td', {'class': 'LblHd'}):
        print(item_name.string)



trade_spider(3)

