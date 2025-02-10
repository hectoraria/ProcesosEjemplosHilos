import threading
import random
import time



class Vocales(threading.Thread):


    def __init__(self,frase, vocal):
        super().__init__()
        self.vocal = vocal
        self.frase = frase

    def run(self):
        vocales = 0
        for l in self.frase:
            if l.lower() == self.vocal:
                vocales = vocales + 1

        print(f"Hay {vocales}, {self.vocal}")




if __name__ == '__main__':

    frase="Hola soy Eduardo no me gusta Marco"

    Vocales(frase,'a').start()
    Vocales(frase,'e').start()
    Vocales(frase,'i').start()
    Vocales(frase,'o').start()
    Vocales(frase,'u').start()


