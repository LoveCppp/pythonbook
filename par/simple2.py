#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple2.py.py
# @Author: For lg224@foxmail.com
# @Date  : 10/4/17

import paramiko
username='root'
password='fewafewa'
hostname="192.168.1.1"
port=22

try:
    t=paramiko.Transport((hostname,port))
    t.connect(username=username,password=password)
    sftp=paramiko.SFTPClient.from_transport(t)
    sftp.put('host/user/info.db','/data/user/info.db')
    sftp.get('/data/userinfo_1.db','/home/user/info_1.db')
    sftp.mkdir('home/userdir',0755)
    sftp.rmdir('home/userdir')
    sftp.rename('/home/test.sh','/home/testfile.sh')
    print sftp.stat('/home/testfile.sh')
    print sftp.listdir('/home')
except Exception,e:
    print str(e)

