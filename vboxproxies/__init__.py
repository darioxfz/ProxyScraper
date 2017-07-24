#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
from itertools import compress
from multiprocessing import Pool,cpu_count
from tqdm import tqdm
from time import sleep

url = ''
session = requests.session()
def about():
    print("Created by...")
    print("                ¸„»°'´¸„»°'´Vorticalbox `'°«„¸`'°«„¸")
    print("`'°«„¸¸„»°'´¸„»°'´`'°«„¸Scientia Potentia est ¸„»°'´`'°«„¸`'°«„¸¸„»°'´")
    print("import vboxproxies as vb")
    print("proxies = vb.getProxies('http://target.com',10)")
    print("returns a list of working proxies and checks with 10 threads")
def getProxies(u,t):
    global url
    url = u
    proxies = get()
    ret=[]
    with Pool(t) as p:
        print("checking proxies against {0} with {1} threads".format(url,t))
        for i in tqdm(p.map(proxyCheck, proxies), total=len(proxies)):
            ret.append(i)
    proxies = list(compress(proxies, ret))
    return proxies
def proxyCheck(p):
    try:
        with session as s:
            r = s.get(url, proxies={'https' :p, 'http':p}, timeout=1)
            if r.status_code == 200:
                return True
            else:
                return False
    except:
        return False

#scrape proxies
def get():
    proxies = []
    urls = ['https://www.us-proxy.org/','https://incloak.com/proxy-list/', 'http://free-proxy-list.net/anonymous-proxy.html', 'http://free-proxy-list.net/']
    print("scraping proxies")
    for u in urls:
        for r in bs(session.get(u).text, 'html.parser').find_all('tr'):
                for i in r.contents[0]:
                    break
                for p in r.contents[1]:
                    l = str(i) + ':' + str(p)
                    if '<input' in l:
                        break
                    else:
                        if 'IP Address' in l:
                            break
                        else:
                            if l not in proxies:
                                proxies.append(l)
    print("found {0}".format(len(proxies)))
    return proxies

if __name__ == '__main__':
    about()
