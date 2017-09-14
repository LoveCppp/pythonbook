#coding:utf-8
import smtplib
import string


HOST = "smtp.qq.com"

SUBJECT ="TEST email from Python"

To="xxx@foxmail.com"
FROM="xxx@qq.com"

text="Python rules them all"

BODY = string.join((

        "From : %s" % FROM,
        "To : %s" % To,
        "Subkect : %s" % SUBJECT,
        "",
        text
    ),"\r\n"
)

server=smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("xxx@qq.com","xxx.")
server.sendmail(FROM,[To],BODY)
server.quit()


