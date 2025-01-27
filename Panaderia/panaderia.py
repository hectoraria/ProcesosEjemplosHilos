import random
import time
from threading import Lock, Thread, Semaphore, Condition


class Panaderia(Thread):
    cond = Condition()
    panes = 7

    def __init__(self):
        Thread.__init__(self)

    def compra_pan(self):
        comprado = False
        with self.cond:
            if Panaderia.panes > 0:
                Panaderia.panes -= 1
                comprado = True

        return comprado

    def reponedor(self):
        reponer=False
        with self.cond:
            if Panaderia.panes == 0:
                Panaderia.panes += 7
                reponer = True

        return reponer



class Cliente(Thread):
    def __init__(self, nombre, panaderia):
        Thread.__init__(self, name=nombre)
        self.panaderia = panaderia

    def run(self):
        print(f"Cliente {self.name} ha entrado")
        time.sleep(random.randint(1, 3))
        if self.panaderia.reponedor():
            print(f"Reponiendo el pan")
        if self.panaderia.compra_pan():
            print(f"Cliente {self.name} ha comprado un pan")
        else:
            print(f"Cliente {self.name} no ha podido comprar un pan")