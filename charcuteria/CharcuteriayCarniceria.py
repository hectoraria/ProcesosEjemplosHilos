from threading import *
from time import *
from random import *


class CarniceriaCharcuteria(Thread):
    carniceros = Semaphore(4)
    charcuteros = Semaphore(2)

    def __init__(self, nombre):
        self.atendido = [False, False]
        Thread.__init__(self, name=nombre)

    def comprarCarniceria(self):
        print(f'{self.name} compra en la carnicería 🥩✔✔')
        sleep(randint(1, 3))
        print(f'{self.name} termina en la carnicería 🥩❌❌')
        self.carniceros.release()
        self.atendido[0] = True

    def comprarCharcuteria(self):
        print(f'{self.name} compra en la charcuteria 🥓✔✔')
        sleep(randint(1, 3))
        print(f'{self.name} termina en la charcuteria 🥓❌❌')
        self.charcuteros.release()
        self.atendido[1] = True

    def run(self):
        sleep(randint(1, 3))
        print(f'{self.name} llega a la tienda')

        while self.atendido[0] == False or self.atendido[1] == False:
            if not self.atendido[0]:
                if self.carniceros.acquire(blocking=False):
                    self.comprarCarniceria()
            if not self.atendido[1]:
                if self.charcuteros.acquire(blocking=False):
                    self.comprarCharcuteria()


if __name__ == '__main__':
    for i in range(1,11):
        hilo = CarniceriaCharcuteria(i)
        hilo.start()