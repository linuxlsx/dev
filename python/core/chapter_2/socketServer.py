#-*- coding:utf-8 -*-
from time import ctime
from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(1)

while True:
    print 'waiting for Connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        #print tcpCliSock.getaddrinfo()
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))
        
    tcpCliSock.close()

tcpSerSock.close()

