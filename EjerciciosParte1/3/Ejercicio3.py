import random
import threading
from threading import Thread


class NumeroAdivinar(threading.Thread):
    valor = random.randint(1, 100)  
    lock = threading.Lock()
    correcto = False

    def __init__(self, nombre, barrera: threading.Barrier):
        super().__init__()
        self.nombre = nombre
        self.barrera = barrera

    def run(self):
        self.barrera.wait()

        while not NumeroAdivinar.correcto:
            numero = random.randint(1, 100)

            with NumeroAdivinar.lock:
                if NumeroAdivinar.correcto:
                    break

                if numero == NumeroAdivinar.valor:
                    NumeroAdivinar.correcto = True
                    print(f"🎯 {self.nombre} ¡Número acertado! Era: {numero}")
                    break


        self.barrera.wait()


if __name__ == "__main__":
    hilos = []
    barrier = threading.Barrier(10)


    for i in range(10):
        hilo = NumeroAdivinar(f"Hilo-{i + 1}", barrier)
        hilo.start()
        hilos.append(hilo)


    for hilo in hilos:
        hilo.join()

    print("🏁 ¡Juego terminado!")
