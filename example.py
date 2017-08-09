#!/usr/bin/python3
import proxyScraper as ps
import requests
import json
from multiprocessing import Pool

def getIP(p):
    session = requests.session()
    with session as s:
        try:
            r = s.get("http://ip-api.com/json", proxies={'https' :p, 'http':p}, timeout=5)
            j = json.loads(r.text)
            print('my IP is {0}'.format(j['query']))
        except:
            print('{0} Failed'.format(p))

proxies = ps.getProxies('https://www.google.co.uk',50)
print("{0} working".format(len(proxies)))
with Pool(50) as p:
    p.map(getIP, proxies)
