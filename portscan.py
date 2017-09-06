#coding:utf-8
import optparse
from socket import *
parser = optparse.OptionParser('usage %prog -H'+'<target host> -p <target port>')
parser.add_option('-H',dest='tgtHost',type='string',help='specfiy target host')
parser.add_option('-p',dest='tgtPort',type='int',help='specify target port')
(options,args)=parser.parse_args()
tgtHost=options.tgHost
tgtPort=options.tgtPort
if tgtHost == None | tgtPort==None:
    print parser.usage
    exit(0)
def coonScan(tgtHost,tgtPort):
    try:
        conSkt=socket(AF_INET,SOCK_STREAM)
        conSkt.connect((tgtHost,tgtHost))
        print '[-] %dtc[ closed'% tgtPort

    except Exception,e:
        

