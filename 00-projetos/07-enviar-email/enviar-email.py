import os
import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(os.getenv('USER_EMAIL'), os.getenv('PASSWORD'))
server.sendmail(
    os.getenv('USER_EMAIL'),
    os.getenv('USE_EMAIL'),
    'TESTE DE MENSAGEM'
)

server.quit()