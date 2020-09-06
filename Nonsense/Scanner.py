from bs4 import BeautifulSoup
import urllib3
import re

http = urllib3.PoolManager()

url = 'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies='

for i in range (65, 65 + 26):
    req = http.request('GET', url + chr(i))

    soup = BeautifulSoup(req.data)

    trs = soup.find(id='main').find_all("tr", class_=re.compile("ts(0|1)"))

    for tr in trs:
        print (tr.find_all("td")[1].string)
