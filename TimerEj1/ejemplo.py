from threading import *



def funcion():
    print("Hola mundo")

if __name__ == "__main__":
    temporizador= Timer(5, funcion)
    temporizador.start()
    print("Esperando...")