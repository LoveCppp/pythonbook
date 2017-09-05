#coding:utf-8

import psutil,datetime

mem=psutil.virtual_memory()

print mem.total,mem.used,mem.free

print psutil.disk_usage('/')
print psutil.disk_io_counters()
#network
print psutil.net_io_counters()
#user login
print psutil.users()

#system run time
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d")
# get all pid
print psutil.pids()
# get pid name
p=psutil.Process(17)
print p.name()
print p.exe()
print p.cwd()
print p.status()
