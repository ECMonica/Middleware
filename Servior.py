import Pyro4
import logging

logging.basicConfig(level=logging.INFO)

@Pyro4.expose
class Multiplicador:
    def multiplicar_por_dos(self, numero):
        resultado = numero * 2
        logging.info(f"El servidor recibió {numero} y devolvió {resultado}")
        return resultado

def main():
    try:
        # Iniciar el servidor Pyro
        daemon = Pyro4.Daemon()
        uri = daemon.register(Multiplicador)

        logging.info("URI del servidor: %s", uri)

        daemon.requestLoop()
    except Exception as e:
        logging.error("Error al iniciar el servidor: %s", e)

if __name__ == "__main__":
    main()