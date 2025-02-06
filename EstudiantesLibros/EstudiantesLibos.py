import time
from random import randint
from threading import Thread, Condition

class Libreria:
    libros = [False, False, False, False, False, False, False]  # False = Disponible, True = Ocupado
    cond = Condition()

class Estudiante(Thread):
    def __init__(self, nombre, libreria):
        super().__init__(name=f"Estudiante-{nombre}")
        self.libreria = libreria

    def run(self):
        libro1 = randint(0, len(self.libreria.libros) - 1)
        libro2 = randint(0, len(self.libreria.libros) - 1)
        while libro1 == libro2:
            libro2 = randint(0, len(self.libreria.libros) - 1)

        with self.libreria.cond:
            while self.libreria.libros[libro1] or self.libreria.libros[libro2]:
                print(f"{self.name} está esperando a que se liberen los libros {libro1} y {libro2}")
                self.libreria.cond.wait()

            # Reservar los libros
            self.libreria.libros[libro1] = True
            self.libreria.libros[libro2] = True

        print(f"{self.name} está usando los libros {libro1} y {libro2}")
        time.sleep(randint(1, 4))
        print(f"{self.name} ha terminado de usar los libros {libro1} y {libro2}")

        with self.libreria.cond:
            self.libreria.libros[libro1] = False
            self.libreria.libros[libro2] = False
            self.libreria.cond.notify_all()  # Notificar a otros hilos que los libros están libres
