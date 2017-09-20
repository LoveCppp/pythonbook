#coding:utf-8
import os,sys
import time
import pycurl


url="http://www.baidu.com"

c=pycurl.Curl()
c.setopt(pycurl.URL,url)
c.setopt(pycurl.CONNECTTIMEOUT,5)
c.setopt(pycurl.TIMEOUT,5)
c.setopt(pycurl.NOPROGRESS,0)
c.setopt(pycurl.MAXREDIRS,5)
c.setopt(pycurl.FORBID_REUSE,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt",'wb')
c.setopt(pycurl.WRITEHEADER,indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)
try:
    c.perform()
except Exception,e:
    print "connecion error "+str(e)
    indexfile.close()
    c.close()
    sys.exit()
NAMELOOKUP_TIME=c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME=c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME =c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME=c.getinfo(c.TOTAL_TIME)
HTTP_CODE =c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD=c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE=c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)


print "http status code : %s" % (HTTP_CODE)
print "DNS RESERV TIME : %.2f ms" % (NAMELOOKUP_TIME*1000)
print "content TIME : %.2f ms" % (CONNECT_TIME*1000)
print "http heade size : %d byte" % (HEADER_SIZE)

indexfile.close()
c.close()
