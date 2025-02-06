from threading import Event
import time
from Carrera import Carrera

if __name__ == '__main__':
    salida = Event()
    salida.clear()
    corredores = [Carrera(f"{i}", salida) for i in range(1, 10)]
    print("La carrera empieza en 3...")
    time.sleep(1)
    print("La carrera empieza en 2...")
    time.sleep(1)
    print("La carrera empieza en 1...")
    time.sleep(1)
    print("💨💨💨💨")
    for c in corredores:
        c.start()

    for c in corredores:
        c.join()
    print("La carrera ha acabado")