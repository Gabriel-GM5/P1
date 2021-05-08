import Pyro4

def main():
    # Registra o nome do servidor
    crud_de_perfis = Pyro4.Proxy("PYRONAME:p1.crud")

    # Lista de operações
    while True:
        print('1 - Adicionar Perfil')
        opt = int(input('Opção desejada: '))
        if opt == 1:
            email = input('E-mail: ')
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            print(crud_de_perfis.novoPerfil(email, nome, sobrenome))
        if opt == 2:
            print(crud_de_perfis.listarPerfis())

if __name__ == "__main__":
    main()