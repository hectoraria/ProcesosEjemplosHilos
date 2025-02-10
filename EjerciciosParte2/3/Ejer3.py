import random
from threading import Semaphore, Thread,Lock
import time

class Cliente(Thread):
    cajero = Semaphore(4)


    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)

    def run(self):
        print(f"🧑‍🦲 Cliente {self.name} está esperando para usar el cajero")
        Cliente.cajero.acquire()
        print(f"🪙 Cliente {self.name} está sacando dinero.")
        time.sleep(random.randint(1,5) )

        Cliente.cajero.release()
        print(f"📤 Cliente {self.name} ha terminado de utilizar el cajero. Cajeros diponibles {self.cajero._value} ")
