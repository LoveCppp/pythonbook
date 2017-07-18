#coding:utf-8
import socket
'''
socket.setdefaulttimeout(2)
s=socket.socket()
try:
    s.connect(('127.0.0.1',22))
    ans=s.recv(1024)

    if "SSH-2.0-OpenSSH_6.6.1" in ans:
        print '[+] SSh server is vulnerable'
except Exception,e:
    print "error"+str(e)

'''


#function

def reBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024)
        return banner
    except:
        return False

def main():
    ip='127.0.0.1'
    port=22
    banner1=reBanner(ip,port)
    if banner1:
        print '[+]'+ip+'banner is : '+banner1

if __name__ == '__main__':
    main()






