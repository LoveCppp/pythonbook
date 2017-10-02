#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple1.py.py
# @Author: For lg224@foxmail.com
# @Date  : 10/2/17
import pxssh
import getpass

try:
    s=pxssh.pxssh()
    hostname=raw_input("hostname:")
    username=raw_input("username:")
    password=getpass.getpass('plase input you plasswd')
    s.login(hostname,username,password)
    s.sendline('uptime')
    s.prompt()
    print s.before
    s.sedline('ls -l')
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh,e:
    print "PXssh failed on login"
    print str(e)