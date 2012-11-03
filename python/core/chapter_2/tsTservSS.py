#-*- coding:utf-8 -*-

#Use SocketServer 

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        data = self.rfile.readline()
        print data
        self.wfile.write('[%s] %s' % (ctime(), data))
tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
