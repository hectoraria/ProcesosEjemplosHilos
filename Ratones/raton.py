# Los ratones tienen que compartir el plato
from threading import Thread, Event
import time
import random
import threading

class Raton(Thread):
    def __init__(self, nombre, evento: Event):
        Thread.__init__(self, name=nombre)
        self.evento = evento

    def run(self):

        # El ratón espera a que el plato se quede libre
        while not self.evento.is_set():
            self.evento.wait()
        self.evento.clear()
        print("El ratón", self.name, "toma el control del plato")
        time.sleep(random.randint(1, 3))
        print("El ratón", self.name, "termina de comer")
        self.evento.set()


if __name__ == '__main__':

    eve = threading.Event()
    eve.set()
    for i in range(1,15):

        e = Raton(i,eve)
        e.start()