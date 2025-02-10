import random
from threading import Semaphore, Thread,Lock
import time

class Cliente(Thread):
    carniceria = Semaphore(4)


    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)

    def run(self):
        print(f"🧑‍🦲 Cliente {self.name} está esperando para ser atendido")
        Cliente.carniceria.acquire()
        print(f"🪙 Cliente {self.name} está siendo atendido.")
        time.sleep(random.randint(1,5) )

        Cliente.carniceria.release()
        print(f"📤 Cliente {self.name} ha terminado en la carniceria.")


if __name__ == '__main__':
    for i in range(1,11):
        c = Cliente(i)
        c.start()