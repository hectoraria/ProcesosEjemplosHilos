import random
from threading import Event, Thread
import time


class Carrera(Thread):
    def __init__(self, name, event: Event):
        Thread.__init__(self, name=name)
        self.event = event

    def run(self):
        inicio = time.time()

        if not self.event.is_set():
            self.event.set()

        print("El corredor", self.name, "comienza a correr")
        time.sleep(random.randint(1, 5))
        print("El corredor", self.name, "llega a la meta")
        self.event.set()
        fin = time.time()
        print("El corredor", self.name, "ha tardado", fin - inicio, "segundos")