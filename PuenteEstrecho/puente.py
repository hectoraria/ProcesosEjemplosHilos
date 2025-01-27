import random
from threading import Semaphore, Thread,Lock
import time

class Vehiculos(Thread):
    capacidad=5
    direccionSur = Semaphore(capacidad)
    direccionNorte= Semaphore(capacidad)


    def __init__(self,nombre,direccion):
        Thread.__init__(self,name=nombre,direccion=direccion)

    def run(self,direccion):

        if direccion == 1:
            print(f"⛽ Vehiculo {self.name} está entrando al por el Sur")
            self.direccionSur.acquire()
            self.direccionNorte.acquire()
            print(f"⛽ Vehiculo {self.name} está entrando al puente")
            self.direccionSur.release()
            self.direccionNorte.release()
            print(f"📤El Vehiculo {self.name} se esta marchando del puente")
        else:
            print(f"⛽ Vehiculo {self.name} está entrando al por el Norte")
            self.direccionNorte.acquire()
            self.direccionSur.acquire()
            print(f"⛽ Vehiculo {self.name} está entrando al puente")
            self.direccionNorte.release()
            self.direccionSur.release()
            print(f"📤El Vehiculo {self.name} se esta marchando del puente")









