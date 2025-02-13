import time
from random import randint
from threading import Thread, Condition
from colorama import Fore



class Platos:
    libros = [False, False, False, False, False, False, False]
    cond = Condition()

class Filosofo(Thread):
    def __init__(self, nombre, platos):
        super().__init__(name=f"Filosofo-{nombre}")

        self.palilloIzq = nombre
        self.palilloDer = nombre + 1

        self.platos = platos

    def run(self):
        time.sleep(randint(3, 7))
        while True:

            print(f"{Fore.GREEN}Ha terminado de estudiar {self.name}")

            plato1 = self.palilloIzq
            plato2 = self.palilloDer


            with self.platos.cond:
                while self.platos.libros[plato1] or self.platos.libros[plato2]:
                    print(f"{Fore.RED}{self.name} está esperando a que se liberen los platillos {plato1} y {plato2}")
                    self.platos.cond.wait()

                if not self.platos.libros[plato1]:
                    self.platos.libros[plato1] = True
                if not self.platos.libros[plato2]:
                    self.platos.libros[plato2] = True

            print(f"{Fore.YELLOW}{self.name} está usando los platillos {plato1} y {plato2}")
            time.sleep(randint(1, 7))
            print(f"{Fore.MAGENTA}{self.name} ha terminado de usar los platillos {plato1} y {plato2}")

            with self.platos.cond:
                self.platos.libros[plato1] = False
                self.platos.libros[plato2] = False
                self.platos.cond.notify_all()

if __name__ == '__main__':
    platos = Platos()
    for i in range(0,5):
        e = Filosofo(i,platos)
        e.start()