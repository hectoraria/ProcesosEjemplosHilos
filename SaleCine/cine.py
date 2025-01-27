import random
from threading import Semaphore, Thread,Lock
import time

class Espectador(Thread):
    semaforo = Semaphore(20)


    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)

    def run(self):
        print(f"🧑‍🦲 Espectador {self.name} está esperando para entrar a la sala de cine")
        Espectador.semaforo.acquire()
        print(f"🎟️ Espectador {self.name} está entrando a la sala. Espacios diponibles {self.semaforo._value}")
        time.sleep(3)
        print(f"📤 Espectador {self.name} se esta marchando de la sala.")
        Espectador.semaforo.release()
