#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool,cpu_count
from tqdm import tqdm

url = ''
session = requests.session()
def about():
    print("Proxy Scraper by...")
    print("                ¸„»°'´¸„»°'´Vorticalbox `'°«„¸`'°«„¸")
    print("`'°«„¸¸„»°'´¸„»°'´`'°«„¸Scientia Potentia est ¸„»°'´`'°«„¸`'°«„¸¸„»°'´")
def getProxies(u,t):
    about()
    global url
    url = u
    proxies = get()
    working = []
    with Pool(t) as p:
        print("checking proxies against {0} with {1} threads".format(url,t))
        for i in tqdm(p.imap_unordered(proxyCheck, proxies), total=len(proxies)):
            if i != False:
                working.append(i)
    return working
def proxyCheck(p):
    try:
        with session as s:
            r = s.get(url, proxies={'https' :p, 'http':p}, timeout=5)
            if r.status_code == 200:
                return p
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
        try:
            for r in bs(session.get(u, timeout=5).text, 'html.parser').find_all('tr'):
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
        except:
            print('connection to {0} failed'.format(u))
        try:
            r = requests.get("https://hidester.com/proxydata/php/data.php?mykey=data&offset=0&limit=100&orderBy=latest_check&sortOrder=DESC&country=&port=&type=undefined&anonymity=undefined&ping=undefined&gproxy=2", headers=headers)
            l = json.loads(r.content)
            for x in l:
                if x['type'] == 'http':
                    proxies.append(':'.join(x['IP'], x['PORT']))
        except:
            print('connection to {0} failed'.format('https://hidester.com/'))
    print("found {0}".format(len(proxies)))
    return proxies
if __name__ == '__main__':
    about()
