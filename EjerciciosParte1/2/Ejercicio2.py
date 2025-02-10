import threading


class Contador:
   def __init__(self):
       self.valor = 0
       self.lock = threading.Lock()



   def incrementar(self, total):
       with self.lock:
           if self.obtener_valor() >= total:
               return
           self.valor += 1



   def obtener_valor(self):
       return self.valor





def incrementar_contador(contador, total):
   while contador.obtener_valor() < total:
       contador.incrementar(total)


if __name__ == "__main__":
   contador = Contador()
   hilos = []
   N = 10
   TOTAL = 1000



   for _ in range(N):
       hilo = threading.Thread(target=incrementar_contador, args=(contador, TOTAL))
       hilos.append(hilo)
       hilo.start()



   for hilo in hilos:
       hilo.join()


   # Mostrar el valor final del contador
   print(f"Valor final del contador: {contador.obtener_valor()}")