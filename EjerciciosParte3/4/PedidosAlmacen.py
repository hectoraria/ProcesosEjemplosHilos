import random
from threading import Thread, Event, Barrier
import time


class Almacen:
    def __init__(self, num_trabajadores):
        self.barrera = Barrier(num_trabajadores)  # Barrera para sincronizar trabajadores
        self.evento = Event()  # Evento para notificar que hay un pedido
        self.pedido_listo = False  # Indicador de si hay un pedido listo

    def generar_pedido(self):
        """Genera un nuevo pedido y despierta a los trabajadores."""
        self.pedido_listo = True
        print("🛒 Nuevo pedido generado. ¡Preparar!")
        self.evento.set()  # Señala que el pedido está listo

    def procesar_pedido(self, nombre_trabajador):
        """Cada trabajador prepara un pedido."""
        while True:
            self.evento.wait()  # Espera a que el evento esté 'set' (pedido listo)

            # El trabajador procesa el pedido
            print(f"{nombre_trabajador} está preparando el pedido.")
            time.sleep(random.randint(2, 5))  # Simula el tiempo de preparación
            self.pedido_listo = False  # El pedido ha sido procesado

            # Después de procesar el pedido, restablece el evento
            self.evento.clear()

            # Simula una pausa antes de que haya otro pedido
            time.sleep(random.randint(1, 3))  # Pausa entre pedidos
            self.generar_pedido()  # Genera un nuevo pedido


class Trabajador(Thread):
    def __init__(self, nombre, almacen):
        super().__init__(name=nombre)
        self.almacen = almacen

    def run(self):
        self.almacen.barrera.wait()  # Sincroniza la barrera antes de comenzar
        print(f"🚀 {self.name} listo para trabajar.")
        self.almacen.procesar_pedido(self.name)  # Procesa los pedidos en un ciclo infinito


if __name__ == "__main__":
    almacen = Almacen(num_trabajadores=5)

    # Crear y lanzar los trabajadores
    for i in range(5):
        Trabajador(f"Trabajador-{i + 1}", almacen).start()

    # Generar algunos pedidos
    for _ in range(3):
        time.sleep(random.randint(2, 5))  # Generar un pedido en intervalos aleatorios
        almacen.generar_pedido()
