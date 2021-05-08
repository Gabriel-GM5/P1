import Pyro4, ZODB, ZODB.FileStorage
'''
# Configuração do ODB
storage = ZODB.FileStorage.FileStorage('data/mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root
'''
@Pyro4.expose
class CrudDePerfis(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is 12345678.".format(name)
    def soma_numeros(self, a, b):
        return a+b

# Configuração da Conexão
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(CrudDePerfis)
ns.register("p1.crud", uri)

# Inicia a recepção de requisições
print("Recebendo")
daemon.requestLoop()