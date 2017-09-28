#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple1.py
# @Author: For lg224@foxmail.com
# @Date  : 9/28/17


import os,sys,time,subprocess
import  warnings,logging

warnings.filterwarnings("ignore",category=DeprecationWarning)
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from  scapy.all import traceroute

domains=raw_input("plase input on or more Ip/domain:")

target=domains.split(' ')
print target
dport=[0]

if len(target) >=1 and target[0] != '':
    res,unas = traceroute(target[0],dport=domains,retry=2)
    res.graph(target=">test.svg")
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert test.svg test.png",shell=True)
else:
        print "IP/domain number of error "