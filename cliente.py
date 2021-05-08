import Pyro4

#name = input("What is your name? ").strip()

crud_de_perfis = Pyro4.Proxy("PYRONAME:p1.crud")    # use name server object lookup uri shortcut
#print(greeting_maker.get_fortune(name))
#print(greeting_maker.soma_numeros(5, 7))
while True:
    print('1 - Soma')
    print('2 - Subtração')
    opt = int(input('Opção desejada: '))
    if opt == 1:
        print(crud_de_perfis.soma_numeros(7, 7))
        