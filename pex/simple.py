#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple.py
# @Author: For lg224@foxmail.com
# @Date  : 10/2/17


import pexpect
import sys

child = pexpect.spawn('ssh root@192.98.11.11')
fout=file('mylog.txt','w')
child.logfile=fout

child.expect("password:")
child.sendline("123456")
child.expect("#")
child.sendline('ls /home')
child.expect("#")





