
# saved as multi-server.py
import Pyro4

@Pyro4.expose
class Multiplicador(object):
      def multiplicar_por_dos(self, numero):
        resultado = numero * 2
        return(f"El servidor recibió {numero} y devolvió {resultado}")
      
Pyro4.Daemon.serveSimple({
    Multiplicador: "multi",
}, host="0.0.0.0" , port=7070, ns=False, verbose=True)
