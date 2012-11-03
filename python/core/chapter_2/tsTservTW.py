#-*- coding:utf-8 -*-

from twisted.internet import protocol, reactor
from time import ctime

HOST = ''
PORT = 21567

client =[]

class TSServProtocol(protocol.Protocol):

    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt
        self.factory.online.append(self)

    def dataReceived(self, data):
        print 'server data reveived...'
        for ol in self.factory.online:
            if ol is not self:
                ol.transport.write('[%s] %s' % (ctime(), data))

    def connectionLost(self, reason):
        self.factory.online.remove(self)

class TSServerFactory(protocol.ClientFactory):
    protocol = TSServProtocol

    def __init__(self):
        self.online = []

#factory = protocol.Factory()
#factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, TSServerFactory())
reactor.run()
