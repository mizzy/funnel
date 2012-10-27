from .factory import *
from twisted.internet import reactor

class Runner():
    reactor.listenTCP(2200, Factory())
    reactor.run()
