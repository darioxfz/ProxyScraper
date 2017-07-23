#!/usr/bin/python3
import vboxproxies as vb
vb.about()
for i in range(5):
    print("")
proxies = vb.getProxies('http://google.co.uk',50)
print("{0} working".format(len(proxies)))
