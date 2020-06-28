import smtplib,  ssl

port = 465 #for ssl
smtp_server = "smtp.gmail.com"
sender = "malviaravi1999@gmail.com"
receiver= "malviaravi0000@gmail.com"
password= "varsha@1994"
message = """From: From person <malviaravi1999@gmail.com>
To : To person < malviaravi0000@gmail.com>
Subject : deployment testing result

testing is failed
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port, context=context) as server:
    server.login(sender , password)
    server.sendmail(sender, receiver,message)
    print ("successfully send message")
