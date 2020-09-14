
# ERROR E231 = no dejar espacio despues de una coma
# ERROR E203 = mucho espacio antes de los ´:´
# ERROR E271 = mucho espacio despues de una palabra reservada
# como en los dos return que hay en el codigo prueba
# ERROR E501 = una linea es muy larga, como la anterior a esta
# ERROR E201 = espacio entre dos parentesis

def funcion_SumaAbsoluta(entrada_1, entrada_2):

    if ((entrada_1) < (entrada_2)):
        return entrada_2 - entrada_1

    else:
        return entrada_1 - entrada_2
