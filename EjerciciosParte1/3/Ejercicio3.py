import random
import threading
import time
from threading import Thread


class NumeroAdivinar(Thread):
    valor = random.randint(1, 100)  # Número a adivinar
    lock = threading.Lock()
    ganador = None  # Almacenará el nombre del hilo ganador

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        while NumeroAdivinar.ganador is None:
            time.sleep(0.1)# Continuar hasta que haya un ganador
            numero = random.randint(1, 100)


            if NumeroAdivinar.ganador is not None:
                 break  # Si ya hay un ganador, salir del bucle

            if numero == NumeroAdivinar.valor:
                NumeroAdivinar.ganador = self.nombre  # Registrar al ganador
                print(f"🎯 {self.nombre} ¡Número acertado! Era: {numero}")
                break  # Salir del bucle si se adivina el número


if __name__ == "__main__":
    hilos = []

    for i in range(10):
        hilo = NumeroAdivinar(f"Hilo-{i + 1}")
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()  # Iniciar todos los hilos

    for hilo in hilos:
        hilo.join()  # Esperar a que todos los hilos terminen

    if NumeroAdivinar.ganador:
        print(f"🏁 ¡El ganador es {NumeroAdivinar.ganador}!")
    else:
        print("🏁 ¡Ningún hilo adivinó el número!")