

from CajeroAutomatico.Cajero import Cliente

if __name__ == '__main__':
    for i in range(1,11):
        c = Cliente(i)
        c.start()