#-*- coding:utf-8 -*-

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        #while True:
            data = raw_input('> ')
            if data:
                print '...sending %s ...' % data
                self.transport.write(data)
            else:
                self.transport.loseConnection()
                #break

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
