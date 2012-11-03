#-*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpServer.recvfrom(BUFSIZ)
    udpServer.sendto('[%s] %s' % (ctime(), data), addr)
    print '...receiver from and return to ' , addr

udpServer.close()


