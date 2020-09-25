import threading
import time
import math


def raices():
    lista = list(range(0, 100000, 1))
    respuesta = []
    for i in lista:
        respuesta.append(math.sqrt(i))
    return respuesta


t0 = time.time()
print(raices(), '\n')
tf = time.time() - t0
print('Tiempo de ejecución: ', tf)
