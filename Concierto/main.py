import threading

from Clases import *

if __name__ == '__main__':

    eve = threading.Event()
    empresaCon=Empresa("EdusMacos",eve)

    ventana = threading.Event()
    for i in range(1, 6):
        e = Comprador(i,eve,ventana)
        e.start()