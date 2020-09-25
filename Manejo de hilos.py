import threading
import time
import math


'''
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
'''

###############################################################

n_threads = 4
inicios = [0, 25000, 50000, 75000]
fines = [25000, 50000, 75000, 100000]
respuesta2 = []


def raices_2(inicio, fin):
    lista2 = list(range(inicio, fin, 1))

    for i in lista2:
        respuesta2.append(math.sqrt(i))
    return respuesta2


'''
paso = len(listaAux)//n_threads
inicios = list()
fines = list()
inicio = 0
fin = paso

for i in range(n_threads):
    inicios.append(inicio)
    fines.append(fin)
    fin += paso
    inicio += paso
'''
t02 = time.time()

threads = list()
for i in range(len(inicios)):
    t = threading.Thread(target=raices_2, args=(inicios[i], fines[i]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

tf2 = time.time() - t02

print(respuesta2)
print('Tiempo de ejecución con 4 hilos: ', tf2)
