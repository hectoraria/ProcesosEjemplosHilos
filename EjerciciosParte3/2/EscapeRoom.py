from threading import *
from time import *
from random import *


class ScapeRoom(Thread):
    claveAdivinada = False
    clave = randint(1000, 9999)
    lock = Lock()

    def __init__(self, nombre, b: Barrier):
        self.b = b
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            with ScapeRoom.lock:
                if ScapeRoom.claveAdivinada:
                    break
                intento = randint(1000, 9999)
                if intento == ScapeRoom.clave:
                    ScapeRoom.claveAdivinada = True
                    print(f'{self.name} ha acertado: {ScapeRoom.clave}!!!🎇🎆🎊🎉')
                else:
                    print(f'{self.name} ha fallado: {intento} 💢⁉❌📛')

        sleep(randint(1, 3))
        print(f"{self.name} ha llegado")
        self.b.wait()
        print(f"{self.name} ha salido")


if __name__ == '__main__':
    b = Barrier(5)
    for i in range(5):
        h = ScapeRoom(f'Jugador {i + 1}', b)
        h.start()