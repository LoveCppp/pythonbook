#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : portscab.py
# @Author: For lg224@foxmail.com
# @Date  : 9/29/17

import sys
import nmap

scan_row=[]

input_data=raw_input("plase inpout host and prot:")
if len(scan_row) !=2:
    print "Input erros,example \"192.168.1.1/24 80\""
    sys.exit(0)
host=scan_row[0]
port=scan_row[1]

try:
    nm=nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found',sys.exc_info()[0])
except:
    print("Unexpected error:",sys.exc_info()[0])
    sys.exit(0)



try:
    nm.scan(hosts=host,arguments=' -v -sS -p '+port)
except Exception,e:
    print "Scan error:" + str(e)

for host in nm.all_hosts():
    print('-------------------------------')
    print('Host : %s (%s)'% (host,nm[host].hostname))
    print('State: %s' % nm[host].state())

for proto in nm[host].all_protocols():
    print('-----------')
    print ('Protocol : %s' % proto)
    lport=nm[host][proto].keys()
    lport.sort()
    for port in lport:
        print('port : %s\tstate : %s' %(port,nm[host][proto][port]['state']))







