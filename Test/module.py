from urllib import request

repcourl = 'http://chart.finance.yahoo.com/table.csv?s=REPCOHOME.BO&a=1&b=12&c=2017&d=2&e=12&f=2017&g=d&ignore=.csv'

def download_stock(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)

    lines = csv_str.split("\\n")
    dest_url=r'repco.csv'

    fw = open(dest_url, 'w')
    fw.write('first line of sample file\n')
    for line in lines:
        fw.write(line + "\n")

    fw.close()

download_stock(repcourl)