import random
from threading import Semaphore, Thread, Lock, Condition, Barrier
import time

class Visitante(Thread):
    montañaRusa = Semaphore(5)
    barrera = Barrier(5)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"Visitante {self.name} llega al parque")
        time.sleep(random.randint(1, 3))

        print(f"🧑‍ Visitante {self.name} está esperando para entrar a la atracción")
        Visitante.montañaRusa.acquire()

        print(f"🎟️ Visitante {self.name} entra a la atracción. Espacios disponibles: {self.montañaRusa._value}")

        Visitante.barrera.wait()


        if Visitante.barrera.wait() == 0:
            print("🎢 La montaña rusa está llena. ¡Iniciando el recorrido!")
            time.sleep(4)
            print("🎢 La montaña rusa ha terminado el recorrido!")

        Visitante.barrera.wait()

        print(f"📤 Visitante {self.name} se baja de la atracción.")
        Visitante.montañaRusa.release()