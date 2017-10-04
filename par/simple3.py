#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple3..py
# @Author: For lg224@foxmail.com
# @Date  : 10/4/17

import paramiko
import os
hostname='192.168.1.1'
usernmae='root'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey=os.path.expanduser('/home/key/id_rsa')
key=paramiko.RSAKey.from_private_key(privatekey)
ssh.connect(hostname=hostname,username=usernmae,pkey=key)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()


