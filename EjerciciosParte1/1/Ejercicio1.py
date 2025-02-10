import threading
import random
import time



class Trabajador(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        while True:

            print(f"Soy {self.nombre} y estoy trabajando")


            time.sleep(random.randint(1, 10))



            print(f"Soy {self.nombre} y he terminado de trabajar")

            time.sleep(1)



if __name__ == '__main__':


    hilos = []

    while True:
        for i in range(0,6):
            hilo = Trabajador(i)
            hilos.append(hilo)
            hilo.start()


        for hilo in hilos:
            hilo.join()


