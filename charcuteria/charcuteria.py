from threading import Thread, Event, Semaphore
import time
import random

class Empresa(Thread,):
    empleados=Semaphore(4)
    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)

    def run(self):

        print(f"Cliente {self.name} entrando a la tienda")
        time.sleep(random.randint(1,3))
        print(f"Cliente {self.name} esta en la tienda")

        with self.empleados:  # Adquiere automáticamente el semáforo y lo libera al salir del bloque
            print(f"Cliente {self.name} está siendo atendido.")
            time.sleep(random.randint(1, 3))  # Tiempo de espera correcto
            print(f"Cliente {self.name} ha terminado en la carnicería.")


if __name__ == '__main__':
    for i in range(1,11):
        c = Empresa(i)
        c.start()