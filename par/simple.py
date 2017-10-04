#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : simple.py
# @Author: For lg224@foxmail.com
# @Date  : 10/4/17
import paramiko

hostname="192.168.1.1"
username="root"
password="fewafewar34"

paramiko.util.log_to_file('syslogin.log')
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()