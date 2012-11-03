#-*- coding:utf-8 -*-

import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = prompt("From: ")
toaddr = prompt("To: ").split()

print "Enter message, end with ^Z(windows): "

msg = ("From: %s\r\nTo: %s\r\n\r\n" % (fromaddr, ", ".join(toaddr)))

while True:
    try:
        line = raw_input()
        if line == '':
            break
    except EOFError:
        break

    if not line:
        break

    msg = msg + line

print "Message length is " + repr(len(msg))

server = smtplib.SMTP('smtp.126.com')
server.set_debuglevel(1)
server.login('lishuxiongwoaini@126.com', 'lsxzhy0206Yes')
#server.starttls()
server.sendmail(fromaddr, toaddr, msg)
server.quit()
