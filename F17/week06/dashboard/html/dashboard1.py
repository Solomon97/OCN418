import sys,traceback,random
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File
from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol, \
    listenWS


N = 20


class BroadcastServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            msg = "{} from {}".format(payload.decode('utf8'), self.peer)
            self.factory.broadcast(msg)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = []

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        print("broadcasting message '{}' ..".format(msg))
        for c in self.clients:
            c.sendMessage(msg.encode('utf8'))
            print("message sent to {}".format(c.peer))


if __name__ == '__main__':
    log.startLogging(sys.stdout)

    ServerFactory = BroadcastServerFactory
    # ServerFactory = BroadcastPreparedServerFactory

    factory = ServerFactory(u"ws://*:9000")
    factory.protocol = BroadcastServerProtocol
    listenWS(factory)

    #webdir = File(".")
    #web = Site(webdir)
    #reactor.listenTCP(80,web)

    class Relay(DatagramProtocol):
        def datagramReceived(self,data,addr):
            print('got {} from {}'.format(data,addr))
            try:
                #self.transport.write(data,addr)
                if len(data) <= 50:     # simple safeguard
                    m = data.decode('ascii')
                    s = m.strip().split(',')
                    if 2 == len(s) and float(s[0]) in range(1,N+1):
                        factory.broadcast(m)
                else:
                    print('message too long')
            except:
                traceback.print_exc()

    reactor.listenUDP(9999,Relay())

    reactor.run()

