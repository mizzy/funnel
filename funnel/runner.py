from twisted.internet import reactor
from twisted.conch.ssh import factory, keys, session, userauth, connection
from twisted.python import components
from twisted.conch import error, avatar
from zope.interface import implements
from twisted.conch.checkers import SSHPublicKeyDatabase
from twisted.cred import portal, checkers
from twisted.python import log
import sys
log.startLogging(sys.stderr)

class Runner():
    def __init__(self, context):
        self.context = context

    def run(self):
        Session.getPty      = self.context.getPty
        Session.execCommand = self.context.execCommand
        Session.openShell   = self.context.openShell
        Session.eofReceived = self.context.eofReceived
        Session.closed      = self.context.closed

        components.registerAdapter(Session, Avatar, session.ISession)

        AuthChecker.checkKey = self.context.authByPublicKey

        Factory.publicKeys['ssh-rsa']  = keys.Key.fromString(self.context.publicKey)
        Factory.privateKeys['ssh-rsa'] = keys.Key.fromString(self.context.privateKey)

        p = portal.Portal(Realm())
        p.registerChecker(AuthChecker())
        Factory.portal = p

        reactor.listenTCP(self.context.port, Factory())
        reactor.run()

class Factory(factory.SSHFactory):
    publicKeys  = {}
    privateKeys = {}
    services = {
        'ssh-userauth': userauth.SSHUserAuthServer,
        'ssh-connection': connection.SSHConnection
     }

class Avatar(avatar.ConchUser):

    def __init__(self, username):
        avatar.ConchUser.__init__(self)
        self.username = username
        self.channelLookup.update({'session':session.SSHSession})

class Session:
    def __init__(self, avatar):
        pass

class Realm:
    implements(portal.IRealm)

    def requestAvatar(self, avatarId, mind, *interfaces):
        return interfaces[0], Avatar(avatarId), lambda: None

class AuthChecker(SSHPublicKeyDatabase):
    pass
