import threading
import time
import math


n_threads = 4  # Cantidad de hilos

# Se crean dos listas que contienen los tramos para cada hilo
inicios = [0, 25000, 50000, 75000]
fines = [25000, 50000, 75000, 100000]
respuesta2 = []


# Función: Calcula la raiz de cada elemento de una lista
# y lo agrega a una lista de salida
# IN: El inicio y el fin para dividir el calculo en 4
# OUT: Retorna respuesta, en este no se necesita, para un hilo si

def raices_2(inicio, fin):
    lista2 = list(range(inicio, fin, 1))  # Crea lista usando los parametros

    for i in lista2:
        # Llena la lista respuesta
        respuesta2.append(format(math.sqrt(i), '.2f'))
    return respuesta2


# Se crea una lista que contiene los hilos creados con el bucle
threads = list()

# Se guarda el tiempo 1
t02 = time.time()
# Bucle que inicia los hilos

for i in range(len(inicios)):
    t = threading.Thread(target=raices_2, args=(inicios[i], fines[i]))
    threads.append(t)
    t.start()

# Bucle que termina cuando todos los hilos han terminado
for t in threads:
    t.join()
# Se hace la diferencia de tiempos
tf2 = time.time() - t02

print(respuesta2)
print('Tiempo de ejecución con 4 hilos: ', tf2)
