# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

HOST = 'smtp.qq.com'
SUBJECT = u"fewafweaf"
TO = "test@qq.com"

FROM = "mymail@gmail.com"



def addimg(src,imgid):
    fp=open(src,'rb')
    msgImage=MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID',imgid)
    return msgImage




msg=MIMEMultipart('related')
msgtext=MIMEText("<body>content</body>")
msg.attach(msgtext)
msg.attach(addimg('img/weekly.png'),'week')


attach=MIMEText(open("doc/week_report.xlsx"),'rb')
attach['Content-type']="application/octet-stream"
attach['Content-Dispostition']="attachment;filename=\"week book\"".decode('utf-8').encode('gb18038')
msg.attach(attach)

msg['Subject']=SUBJECT
msg['From']=FROM
msg['To']=TO



try:
    server = smtplib.SMTP()
    server.connect(HOST, '25')
    server.starttls()
    server.login("xxx@qq.com", '123456')
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print '111'
except Exception, e:
    print 'error' + str(e)

