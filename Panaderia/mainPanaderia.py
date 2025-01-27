from panaderia import *
from random import *

if __name__ == '__main__':
    for i in range(1,101):
        e = Cliente(i,Panaderia())
        e.start()