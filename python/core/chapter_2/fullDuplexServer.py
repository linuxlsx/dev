#-*- coding:utf-8 -*-

from twisted.internet import protocol, reactor
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class ChatServerProtocol(
client = []

chatServer = socket(AF_INET, SOCK_STREAM)
chatServer.bind(ADDR)
chatServer.listen(5)

while True:
    clientSock, addr = chatServer.accept()
    print '...connected from:', addr
    client.append(clientSock)
