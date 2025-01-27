import threading
import queue
import time
import random

def atender_cliente(id_caja, cola_clientes, cajas, lock):
    while not cola_clientes.empty():
        try:
            # Sacar al siguiente cliente de la cola
            cliente = cola_clientes.get(timeout=0.1)
            print(f"Caja {id_caja} está atendiendo al cliente {cliente['id']} durante {cliente['tiempo']} segundos.")

            # Simular el tiempo de atención del cliente
            time.sleep(cliente['tiempo'])

            # Registrar que esta caja atendió a un cliente
            with lock:
                cajas[id_caja] += 1

            print(f"Caja {id_caja} terminó de atender al cliente {cliente['id']}.")

        except queue.Empty:
            break

def ejecutar_simulacion(num_cajas, clientes):

    cola_clientes = queue.Queue()
    for cliente in clientes:
        cola_clientes.put(cliente)

    # Crear contadores para cada caja y un lock
    cajas = [0] * num_cajas
    lock = threading.Lock()

    # Crear y lanzar hilos para las cajas
    threads = []
    for i in range(num_cajas):
        thread = threading.Thread(target=atender_cliente, args=(i, cola_clientes, cajas, lock))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    print("\nSimulación completada.")
    return cajas

if __name__ == "__main__":
    # Número de cajas registradoras
    NUM_CAJAS = 3

    # Crear lista de clientes con tiempos de atención aleatorios
    NUM_CLIENTES = 10
    clientes = [
        {"id": i + 1, "tiempo": random.uniform(1, 5)}  # Tiempo de atención entre 1 y 5 segundos
        for i in range(NUM_CLIENTES)
    ]

    # Mostrar los clientes generados
    print("Clientes generados:")
    for cliente in clientes:
        print(f"Cliente {cliente['id']}: {cliente['tiempo']:.2f} segundos")

    # Medir el tiempo total de la simulación
    inicio = time.time()
    cajas = ejecutar_simulacion(NUM_CAJAS, clientes)
    fin = time.time()

    # Resultados
    tiempo_total = fin - inicio
    print(f"\nTiempo total de atención: {tiempo_total:.2f} segundos")
    for i, atendidos in enumerate(cajas):
        print(f"Caja {i} atendió a {atendidos} clientes.")