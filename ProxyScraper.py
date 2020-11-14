#Importing modules.

import urllib.request
import requests

#Setting timeout.

timeout = 10000 [Put your time out]

#Scraping program.

proxytype = ["HTTP","Socks4","Socks5"]
for x in proxytype:
    proxies = requests.get('https://api.proxyscrape.com?request=amountproxies&proxytype={}'.format(x))
    url = 'https://api.proxyscrape.com?request=getproxies&proxytype={}&timeout={}'.format(x,timeout)
    print('Scraping '+ proxies.text +'\t' + x + ' proxies...')
    urllib.request.urlretrieve(url, '{}.txt'.format(x))