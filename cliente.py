import Pyro4
import logging
import Pyro4

ipAdressServer ="192.168.27.148"

numero = input("Ingresa un número ").strip()

Multiplicador = Pyro4.core.Proxy('PYRO:multi@' + ipAdressServer + ':7070')    
print(Multiplicador.multiplicar_por_dos(numero)
