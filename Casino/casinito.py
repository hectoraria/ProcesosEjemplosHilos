import threading
import random
import time

# Constantes
NUM_JUGADORES = 6
MIN_JUGADORES_PARA_GIRAR = 3

# Sincronización
ruleta_lock = threading.Lock()  # Controla el acceso a la ruleta
jugadores_listos = threading.Semaphore(0)  # Contador de jugadores listos
barrier = threading.Barrier(MIN_JUGADORES_PARA_GIRAR)  # Barrera para esperar a 3 jugadores
croupier_listo = threading.Event()  # Evento para notificar a los jugadores que la ruleta ha girado
resultado_ruleta = None  # Variable compartida para el resultado de la ruleta


def croupier():
    global resultado_ruleta
    while True:
        # Esperar a que al menos 3 jugadores estén listos
        for _ in range(MIN_JUGADORES_PARA_GIRAR):
            jugadores_listos.acquire()

        print("\nCroupier: Girando la ruleta...")
        time.sleep(2)  # Simular el tiempo que toma girar la ruleta
        resultado_ruleta = random.randint(0, 36)
        print(f"Croupier: El resultado es {resultado_ruleta}!")

        # Notificar a los jugadores que la ruleta ha girado
        croupier_listo.set()
        croupier_listo.clear()  # Resetear el evento para la próxima ronda


def jugador(id_jugador):
    while True:
        # Esperar a que la ruleta esté disponible
        with ruleta_lock:
            print(f"Jugador {id_jugador}: Haciendo su apuesta...")
            time.sleep(1)  # Simular el tiempo que toma hacer una apuesta

        # Notificar al croupier que está listo
        jugadores_listos.release()

        # Esperar a que haya al menos 3 jugadores listos
        barrier.wait()

        # Esperar a que el croupier gire la ruleta
        croupier_listo.wait()

        # Recibir el resultado y determinar si gana o pierde
        apuesta = random.randint(0, 36)
        print(f"Jugador {id_jugador}: Apostó al {apuesta}, resultado {resultado_ruleta}")
        if apuesta == resultado_ruleta:
            print(f"Jugador {id_jugador}: ¡Ganó!")
        else:
            print(f"Jugador {id_jugador}: Perdió.")

        # Decidir si sigue jugando o se retira
        if random.random() < 0.2:  # 20% de probabilidad de retirarse
            print(f"Jugador {id_jugador}: Se retira del casino.")
            break
        else:
            print(f"Jugador {id_jugador}: Continúa jugando.")


# Crear e iniciar los hilos del croupier y los jugadores
croupier_thread = threading.Thread(target=croupier)
croupier_thread.daemon = True  # El croupier se ejecuta en segundo plano
croupier_thread.start()

jugadores = []
for i in range(NUM_JUGADORES):
    jugador_thread = threading.Thread(target=jugador, args=(i + 1,))
    jugadores.append(jugador_thread)
    jugador_thread.start()


for jugador_thread in jugadores:
    jugador_thread.join()

print("El casino ha cerrado.")