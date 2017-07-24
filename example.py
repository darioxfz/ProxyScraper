#!/usr/bin/python3
import vboxproxies as vb
import requests
import json
session = requests.session()
for i in range(5):
    print("")
proxies = vb.getProxies('http://google.co.uk',50)
print("{0} working".format(len(proxies)))
for p in proxies:
    with session as s:
        try:
            r = s.get("http://ip-api.com/json", proxies={'https' :p, 'http':p}, timeout=1)
            j = json.loads(r.text)
            print(j['query'])
        except:
            print('{0} Failed'.format(p))
