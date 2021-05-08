import Pyro4, ZODB, ZODB.FileStorage, transaction

# Configuração do ODB
storage = ZODB.FileStorage.FileStorage('data/mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

if not hasattr(root, 'perfis'):
    root.perfis = []
    transaction.commit()

class Perfil:
    def __init__(self, email, nome, sobrenome):
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def getSobrenome(self):
        return self.sobrenome

# Procedimentos
@Pyro4.expose
class CrudDePerfis(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is 12345678.".format(name)
    def soma_numeros(self, a, b):
        return a+b
    def novoPerfil(self, email, nome, sobrenome):
        root.perfis.append(Perfil(email, nome, sobrenome))
        transaction.commit()
        return "Inserido com Sucesso!"
    def listarPerfis(self):
        print(root.perfis)
        ans = ''
        for i in root.perfis:
            ans += 'Nome: ' + i.getNome() + '\nSobrenome: ' + i.getSobrenome() + '\nE-mail: ' + i.getEmail() + '\n'
        return ans

def main():
    # Configuração da Conexão
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(CrudDePerfis)
    ns.register("p1.crud", uri)

    # Inicia a recepção de requisições
    print("Recebendo")
    daemon.requestLoop()

if __name__ == "__main__":
    main()