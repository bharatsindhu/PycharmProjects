import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    fullname = str(name) + '.jpg'
    urllib.request.urlretrieve(url, fullname)

download_web_image("http://cdn.kimaya.in/media/catalog/product/cache/1/image/405x405/040ec09b1e35df139433887a97daa66f/a/n/ant012-mi-3-1856x2784.jpg")