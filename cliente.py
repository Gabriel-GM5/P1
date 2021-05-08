import Pyro4

def main():
    # Registra o nome do servidor
    crud_de_perfis = Pyro4.Proxy("PYRONAME:p1.crud")

    # Lista de operações
    while True:
        print('1 - Soma')
        opt = int(input('Opção desejada: '))
        if opt == 1:
            print(crud_de_perfis.soma_numeros(7, 7))
            