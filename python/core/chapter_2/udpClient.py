#-*- coding:utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpClient = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break

    udpClient.sendto(data, ADDR)
    
    data, addr = udpClient.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpClient.close()

