import time
from http.cookiejar import liberal_is_HDN
from random import random,randint
from threading import Thread, Condition


class Libreria(Thread):
    libros = ["Node","Js","Nada","Tete","Edu","Normandia","Berlin","Pearl Harbor","Marco Polo"]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)




class Estudiante(Thread):
    def __init__(self, nombre, libreria):
        Thread.__init__(self, name=nombre)
        self.libreria = libreria

        def run(self):
            # Se genera una posición aleatoria de la lista
            num = randint(0, 4)

            # Mientras el objeto esté siendo usado por otro hilo no lo puede usar el actual
            with self.libreria.cond:
                while self.libreria.libros[num] == True:
                    print("El hilo", self.name, "está esperando a que se libere la posición", num)
                    Lista.cond.wait()

                # Una vez que su posición está libre la bloquea
                Lista.lista[num] = True

            print("El hilo", self.name, "está usando el objeto", num)
            time.sleep(randint(1, 4))
            print("El hilo", self.name, "ha terminado de usar el objeto", num)

            with Lista.cond:
                Lista.lista[num] = False
                # Notificamos al resto de hilos de que se ha liberado una posición
                Lista.cond.notifyAll()