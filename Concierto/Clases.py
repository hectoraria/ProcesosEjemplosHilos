# Los ratones tienen que compartir el plato
from threading import Thread, Event
import time
import random

class Empresa(Thread,):
    def __init__(self,):
        Thread.__init__(self)
        self.entrada = Event()
        self.ventana = Event()
    def run(self):
        print("Compra disponible.")
        self.entrada.set()
        self.ventana.set()

        time.sleep(3)

        self.entrada.clear()
        self.ventana.clear()

        print("Compra cerrada.")

class Comprador(Thread):
    def __init__(self, nombre,em:Empresa()):
        Thread.__init__(self, name=nombre)

    def run(self):
        compra=True
        while not self.entrada.is_set() or not self.ventana.is_set():
            print("El comprador", self.name, "esta esperando para comprar. 🛑")
            self.entrada.wait(5)
        if compra:
            self.entrada.clear()
            print("El comprador", self.name, "esta comprando el ticket.🎟️")
            time.sleep(1)
            print("El comprador", self.name, "termina de comprar.📤")
            if self.entrada.is_set():
                self.entrada.set()
        else:
            print("El comprador", self.name, "no ha comprado.")
