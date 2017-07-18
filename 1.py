#coding:utf-8

banner='FreeFloat FTP SERVER'

#upper
print banner.upper()

#lower
print banner.lower()
#replase

print banner.replace('FreeFloat','Ability')

#Find

print banner.find('FTP')



#list


portList=[]

portList.append(21)
portList.append(80)
portList.append(443)
portList.append(3389)

print portList

pos=portList.index(80)

print "[+] There are "+str(pos) +" ports to scan before 80 ."

cnt=len(portList)

print cnt



#dict

service = {'ftp':21,'ssh':22,'smtp':25,'http':80}

print service.keys()

print service.items()


print service.has_key('ftp')

print service['ftp']

