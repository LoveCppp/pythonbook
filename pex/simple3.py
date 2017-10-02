#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple3.py.py
# @Author: For lg224@foxmail.com
# @Date  : 10/2/17


import pexpect
import sys

ip="192.168.1.121"
user="root"
passowrd="HFEWAFEWA331@342"
target_file="/data/logs/nginx_access.log"

child=pexpect.spawnu('/usr/bin/ssh',[user+'@'+ip])
fout=file('mylog.txt','w')
child.logfile=fout
try:
    child.expect('(?i)password')
    child.sendline(passowrd)
    child.expect("#")
    child.sendline('tar -czf /data/nginx_access.tar.gz '+target_file)
    child.expect("#")
    print child.before
    child.sendline('exit')
except EOFError:
    print "expect EOF"
except RuntimeError:
    print "expect TIMEOUT"

child=pexpect.spawn('/usr/bin/scp',[user+'@'+ip+':/data/nginx_access.tar.gz','/home'])
fout=file('mylog.ext','a')
child.logfile=fout
try:
    child.expect('(?i)password')
    child.sendline(passowrd)
    child.expect(pexpect.EOF)
except EOFError:
    print 'expect'
