#coding:utf-8
from IPy import IP
ip_s=raw_input('plase input an Ip pr net-range:')

ips=IP(ip_s)

if len(ips) >1 :
    print('net: %s' % ips.net()) #networkaddres
    print('netmask: %s' % ips.netmask()) #netmask
    print('broadcast: %s' % ips.broadcast())  #broadcast
    print('reverse addres %s' % ips.reverseName()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse addres : %s' % ips.reverseName()[0])
print('hexadcimall: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())


