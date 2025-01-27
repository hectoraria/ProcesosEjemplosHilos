from puente import *
from random import *

if __name__ == '__main__':
    for i in range(1,4):
        e = Vehiculos(i,random.randint(1,2))
        e.start()