#coding:utf-8
import smtplib
from email.mime.text import MIMEText



HOST='smtp.qq.com'
SUBJECT=u"fewafweaf"
TO="test@qq.com"

FROM="mymail@gmail.com"

msg= MIMEText("""
    <table width="800" border="0" >
        <tr>
            <td>ffeff</td>
        </tr>
    </table>
""")
msg['Subject']=SUBJECT
msg['from']=FROM
msg['to']=TO
try:
    server=smtplib.SMTP()
    server.connect(HOST,'25')
    server.starttls()
    server.login("xxx@qq.com",'123456')
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
    print '111'
except Exception,e:
    print 'error'+str(e)
    
