import random
import time
from threading import Thread, Barrier


class Peaton(Thread):
    def __init__(self, nombre, barrera: Barrier):
        super().__init__(name=f"Peatón-{nombre}")
        self.barrera = barrera

    def run(self):
        print(f"🚶‍♂️ {self.name} llega al cruce y espera.")
        time.sleep(random.randint(1, 3))  # Simula el tiempo de llegada al cruce

        print(f"⏳ {self.name} esperando el semáforo...")
        self.barrera.wait()  # Espera a que todos los peatones lleguen

        print(f"✅ {self.name} cruza la calle.")
        time.sleep(random.randint(2, 4))  # Simula el tiempo de cruce
        print(f"🏁 {self.name} ha cruzado.")


if __name__ == "__main__":
    NUM_PEATONES = 10  # Total de peatones
    BARRERA_PEATONES = 5  # Número de peatones que cruzan por ciclo

    barrera = Barrier(BARRERA_PEATONES)
    hilos = []

    for i in range(NUM_PEATONES):
        hilo = Peaton(i + 1, barrera)
        hilo.start()
        hilos.append(hilo)
        time.sleep(random.uniform(0.5, 1.5))  # Simula la llegada aleatoria de peatones

    for h in hilos:
        h.join()

    print("\n🚦 Todos los peatones han cruzado.")
