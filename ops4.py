#coding:utf-8

import dns.resolver

domain=raw_input('plase input an domain')
A=dns.resolver.query(domain,'A')
for i in A.response.answer:
    for j in i.items:
        print j.address

Mx=dns.resolver.query(domain,'MX')
for i in Mx:
    print 'Mx preference = ',i.preference,'mail exchanger=' ,i.exchange

NS=dns.resolver.query(domain,'ns')

for i in NS.response.answer:
    for j in i.items:
        print j.to_text()


cname=dns.resolver.query(domain,'CNAME')

for i in cname.response.anser:
    for j in i.items:
        print j.to_text()
