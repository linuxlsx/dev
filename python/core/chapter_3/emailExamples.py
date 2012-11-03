#-*- coding:utf-8 -*-
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

SENDER = 'lishuxiongwoaini@126.com'
RECIPS = ['linuxlsx@gmail.com']
PASSWD = ''
SOME_IMG_FILE = 'd:/picture/1.jpg'

def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello World!</h4>'
        '</body></html>', 'html')
    email.attach(html)
    return email

def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition',
                     'attachemet; filename="%s"' % fn)
    return email

def sendMsg(fr, pw, to, msg):
    s = SMTP('smtp.126.com')
    s.login(fr, pw)
    errs = s.sendmail(fr, to, msg)
    s.quit()

if __name__ == '__main__':
    print 'Sending multipart alternative msg...'
    msg = make_mpa_msg()
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER, PASSWD, RECIPS, msg.as_string())

    print 'Sending image msg...'
    msg = make_img_msg(SOME_IMG_FILE)
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'image file test'
    #sendMsg(SENDER, PASSWD, RECIPS, msg.as_string())
    
    

