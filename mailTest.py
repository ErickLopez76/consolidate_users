__author__ = 'erick_sis'
import smtplib

msg_header = 'From: Sender Name <sender@server>\n' \
             'To: Receiver Name <receiver@server>\n' \
             'Cc: Receiver2 Name <receiver2@server>\n' \
             'MIME-Version: 1.0\n' \
             'Content-type: text/html\n' \
             'Subject: Any subject\n'
title = 'My title'
msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(
    title=title)
msg_full = (''.join([msg_header, msg_content])).encode()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('ericklopez76@gmail.com', 'Evrk1131*-')
server.sendmail('ericklopez76@gmail.com',
                ['elopez@inclusionsocial.gob.sv', 'elopez@inclusionsocial.gob.sv'],
                msg_full)
server.quit()