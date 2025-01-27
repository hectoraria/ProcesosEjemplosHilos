# Saldo compartido
import threading
import time

saldo_cuenta = 1000  # Saldo inicial

def retirar_dinero(cantidad):
    global saldo_cuenta
    if saldo_cuenta >= cantidad:
        # Simula un retraso en la operación
        time.sleep(0.00005)
        saldo_cuenta -= cantidad
        print(f"Retiro exitoso: {cantidad}. Saldo restante: {saldo_cuenta}\n")
    else:
        print(f"Saldo insuficiente para retirar {cantidad}. Saldo actual: {saldo_cuenta}\n")

def depositar_dinero(cantidad):
    global saldo_cuenta
    # Simula un retraso en la operación
    #time.sleep(0.0001)
    saldo_cuenta += cantidad
    print(f"Depósito exitoso: {cantidad}. Saldo actual: {saldo_cuenta}\n")

if __name__ == "__main__":
    # Crear hilos para realizar depósitos y retiros
    hilos = []
    for _ in range(10):
        hilos.append(threading.Thread(target=retirar_dinero, args=(300,)))  # Retira 300
        hilos.append(threading.Thread(target=depositar_dinero, args=(200,)))  # Deposita 200

    # Iniciar todos los hilos
    for hilo in hilos:
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print(f"Saldo final de la cuenta: {saldo_cuenta}")
