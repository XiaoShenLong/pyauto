import smtplib


HOST = "smtp.163.com"
SUBJECT = "Test email from Python"
TO = "xxxxxxxxxxx@qq.com"
FROM = "xxxxxxxx@163.com"
text = "Python rules them all!"
BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ))
server = smtplib.SMTP()
server.connect(HOST,"25")
server.login("xxxxxxxx@163.com","xxxxxxxxx")
server.sendmail(FROM, [TO], BODY)
server.quit()