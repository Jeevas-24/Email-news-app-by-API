import smtplib, ssl
import os
def send_mail(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'jeevasathappan2000@gmail.com'
    password = os.getenv('PASSWORD')
    receiver = 'jeevasathappan2000@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_mail(message='hi')