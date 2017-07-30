# ProxyScraper
module for a quick why to return a list of working proxies

#Requirements
1. BeautifulSoup4 (pip3 install beautifulsoup4)
2. tqdm (pip3 install tqdm)
3. only tested in python3

#usage 

import vboxproxies as vb
proxies = vb.getProxies('http(s)://google.co.uk', 50)
