
import time
import math

# Funcion: Calcula las raices de todos los elementos de un array de un
# dimención del 0 al 100000
# IN: no recibe parámetros
# OUT: retorna una lista con las raices de los elementos de la lista de
# 0 al 100000


def raices():
    # Se genera una lista del 0 al 100000 con saltos de 1
    lista = list(range(0, 100000, 1))
    respuesta = []
    for i in lista:
        # Se agregan las raices a la lista de salida
        respuesta.append(format(math.sqrt(i), '.2f'))
    return respuesta  # Con dos decimales


# con la función time se toma el tiempo hasta t0
t0 = time.time()

print(raices(), '\n')

tf = time.time() - t0  # Se hace la diferencia de tiempo


print('Tiempo de ejecución: ', tf)
