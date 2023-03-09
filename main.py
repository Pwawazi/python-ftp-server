from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("Inferno", "abcde")
checker.addUser("Dante", "12345")
checker.addUser("Abigail", "12345")

portal = Portal(FTPRealm("./public", "./myUsers"), [AllowAnonymousAccess(), checker])

factory = FTPFactory(portal)

reactor.listenTCP(23, factory)
reactor.run()