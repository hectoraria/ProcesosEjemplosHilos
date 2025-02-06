from EstudiantesLibos import *
from random import *

if __name__ == '__main__':
    libreria = Libreria()
    for i in range(1,11):
        e = Estudiante(i,libreria)
        e.start()