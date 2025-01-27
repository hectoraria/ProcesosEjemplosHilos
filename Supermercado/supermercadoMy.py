import threading
import time


def descargar_archivo(nombre, tiempo):
    print(f"Iniciando descarga de {nombre}")
    time.sleep(tiempo)  # Simula tiempo de descarga
    print(f"Descarga de {nombre} completada")

if __name__ == "__main__":
    hilos = [
        threading.Thread(target=descargar_archivo, args=("Archivo 1", 3)),
        threading.Thread(target=descargar_archivo, args=("Archivo 2", 5)),
        threading.Thread(target=descargar_archivo, args=("Archivo 3", 2)),
    ]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print("Todas las descargas finalizadas")
