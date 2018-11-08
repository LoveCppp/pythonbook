#coding:utf-8
from netaddr import *
from IPy import IP

startip = '123.125.115.110'
endip = '123.125.115.112'

cidrs = iprange_to_cidrs(startip, endip)

for iprange in cidrs:
    ip = str(iprange)
    ips = IP(ip)
    for x in ips:
        print x    
