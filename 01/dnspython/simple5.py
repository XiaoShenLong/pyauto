import dns.resolver
import requests

domain = "www.google.com.hk"
iplist = []

def getip(domain):
    try:
        A = dns.resolver.query(domain, 'A')
    except Except as e:
        print('dns resolver error:'+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(url):
    checkurl = "http://" + url + ":80"
    try:
        r = requests.get(checkurl, timeout=5)
        getcontent = r.text[:15]
    finally:
        if getcontent=="<!doctype html>":
            print(ip+" [OK]")
        else:
            print(ip+" [Error]")

if __name__ == "__main__":
    if getip(domain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error.")
