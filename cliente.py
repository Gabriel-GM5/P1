"""
import Pyro4

ns=Pyro4.locateNS()
uri=ns.lookup('obj')
o=Pyro4.Proxy(uri)

print(o.saludar())
"""
# saved as greeting-client.py
import Pyro4

name = input("What is your name? ").strip()

greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut
print(greeting_maker.get_fortune(name))
