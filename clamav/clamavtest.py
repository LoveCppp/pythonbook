#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : clamavtest.py
# @Author: For lg224@foxmail.com
# @Date  : 9/29/17


import time
import pyclamd
from threading import Thread

class Scan(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.IP=IP
        self.scan_type=scan_type
        self.file=file
        self.connstr=""
        self.scanresult=""
    def run(self):
        try:
            if cd.ping():
                cd= pyclamd.ClamdNetworkSocket(self.IP,3310)
                cd.reload()
                if self.scan_type == "contscan_file":
                    self.scanresult="{0}\n".format(cd.contscan_file(self.file))
                elif self.scan_type=="multiscan_file":
                    self.scanresult="{0}\n".format(cd.multiscan_file(self.file))
                elif self.scan_type=="scan_file":
                    self.scanresult="{0}\n".format(cd.scan_file(self.file))
                time.sleep(1)
            else:
                self.connstr=self.IP+"ping error,exit"
                return
        except Exception,e:
            self.connstr=self.IP+" "+str(e)
Ips=['192.168.99.193','192.168.99.191']

scantype="multiscan_file"

scanfile="/data/www"


i=1

threadnum=2


scanlist=[]

for ip in Ips:
    currp=Scan(ip,scantype,scanfile)
    scanlist.append(currp)
    if i%threadnum==0 or i ==len(Ips):
        for task in scanlist:
            task.start()
        for task in scanlist:
            task.join()
            print task.connstr
            print task.scanresult
        scanlist=[]
    i+=1
    void=open('/tmp/EICAR','w').write(cd.EICAR())


