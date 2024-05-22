import Pyro4
import logging

logging.basicConfig(level=logging.INFO)

def main():
    try:
       
        multiplicador = Pyro4.Proxy("PYRO:obj_077901fcaeb046e7bab7218d8665e36b@localhost:58375")

        numero = 7
        resultado = multiplicador.multiplicar_por_dos(numero)

        logging.info(f"El cliente envió {numero} y recibió {resultado}")
    except Exception as e:
        logging.error("Error al conectar con el servidor: %s", e)

if __name__ == "__main__":
    main()
