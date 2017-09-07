#coding:utf-8
import dns.resolver
import os
import requests

iplist=[]

appdomain="www.baidu.com"

def get_iplist(domain=""):
    try:
        A=dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns reslover error:"+str(e)
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def check(ip):
    checkurl=ip+":80"
    getcontent=""
    try:
        r=requests.get(checkurl)
        getcontent=r.text
    finally:
        if getcontent =="<!doctyoe html>":
            print ip+" [ok]"
        else:
            print ip + " [Error]"
if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            check(ip)
        else:
            print "dns resolver error"


