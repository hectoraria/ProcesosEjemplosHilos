# Saldo compartido
import threading
import time

def servir_cafe():
    for i in range(5):
        print(f"Camarero: Sirviendo café {i + 1}")
        time.sleep(1)
    print("Camarero: Terminó de servir todos los cafés")

def poner_tostadas():
    for i in range(5):
        print(f"Camarero: Poniendo tostada {i + 1}")
        time.sleep(2)
    print("Camarero: Terminó de poner todas las tostadas")

def hacer_tortilla():
    for i in range(5):
        print(f"Camarero: Haciendo tortilla {i + 1}")
        time.sleep(3)
    print("Camarero: Terminó de hacer todas las tortillas")

if __name__ == "__main__":

    hilo_cafe = threading.Thread(target=servir_cafe)
    hilo_tostadas = threading.Thread(target=poner_tostadas)
    hilo_tortilla = threading.Thread(target=hacer_tortilla)

    hilo_cafe.start()
    hilo_tostadas.start()
    hilo_tortilla.start()

    hilo_cafe.join()
    hilo_tostadas.join()
    hilo_tortilla.join()
