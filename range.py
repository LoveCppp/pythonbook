#coding:utf-8


portList=[21,22,25,80,110]

for x in range(1,255):
    for port in portList:
        print "[+] checking 192.168.96." + str(x) + ": "+str(port)

