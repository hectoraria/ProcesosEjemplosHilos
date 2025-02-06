import random
from threading import Thread, Barrier
import time


class Caja(Thread):
    def __init__(self,nombre,barrera:Barrier):
        Thread.__init__(self)
        self.barrera = barrera


    def run(self):
        self.barrera.wait()
        print("Hilo", self.name,"entra en caja")
        time.sleep(random.randint(1,3))
        print("Hilo", self.name,"sale en caja")

if __name__ == "__main__":
    barrera=Barrier(5)
    hilos=[]

    for i in range(10):
        hilo = Caja(str(i),barrera)
        time.sleep(random.randint(1,3))
        hilo.start()
        hilos.append(hilo)
    for h in hilos:
        h.join()