#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple2.py.py
# @Author: For lg224@foxmail.com
# @Date  : 10/2/17

from  __future__ import  unicode_literals
import pexpect
import sys

child=pexpect.spawnu('ftp ftp.openbsd.org')
child.expect('(?i)name .*: ')
child.sendline('anonymous')
child.expect('(?i)password')
child.sendline('pexpect@test.net')
child.expect('ftp>')
child.sendline('bin')
child.sendline('ftp>')
child.sendline('get robots.txt')
child.expect('ftp >')
sys.stdout.write(child.before)
print("Escapte character is '^'].\n")
sys.stdout.write(child.after)
sys.stdout.flush()
child.interact()
child.sendline('bye')
child.close()



