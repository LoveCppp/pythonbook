#coding:utf-8
from IPy import IP

#GET IP TYPE

print  IP('10.0.0.0').version() # 4
#ipv4


#ipv6
print  IP('::1').version() #6

ip=IP('192.168.1.0/24')

print ip.len()

for x in ip:
    print(x)

#get ip tpye

print IP('8.8.8.8').iptype() #public

print IP('192.168.8.8').iptype() #priovsate


print IP('192.168.1.0/24').strNormal(3)


print '192.168.1.100' in IP('192.168.1.0/24')

