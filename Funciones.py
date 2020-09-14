# Función: realiza 4 operaciones distintas con dos operandos(+,-,&,|).
# Entrada: dos enteros entre -127 y 127 y un indicador de operación del 0 al 3.
# Salida: Retorna el resultado de la operación o un codigo si hay error.
def basic_ops(num_1, num_2, operator):
    # Verifica que los operandos sean un entero.
    if (type(num_1) != int):
        return '01'
    if (type(num_2) != int):
        return '01'
    # Verifica que los operandos valgan entre -127 y 127.
    if ((num_1 > 127) | (num_2 > 127) | (num_1 < -127) | (num_2 < -127)):
        return '02'
    # Verifica el ingreso de operación que sea entero, entre 0 y 3.
    if (type(operator) != int):
        return '03'
    if((operator > 3) | (operator < 0)):
        return '03'
    # Elige la operación a realizar según el valor del parámetro 'operator'
    if (operator == 0):
        return num_1 + num_2
    if (operator == 1):
        return num_1 - num_2
    if (operator == 2):
        return num_1 & num_2
    if (operator == 3):
        return num_1 | num_2


# Función: realiza 4 operaciones (+,-,&,|) entre los elementos de cada array.
# Entradas: Dos arrays, cuyos elementos cumplen las restricciones de basic_ops.
# Salidas: Array con los resultados de las operaciones, o un código de error.
def array_ops(array_1, array_2, operator):
    # Verifica el tamaño de los arrays de entrada sea el mismo.
    if(len(array_1) != len(array_2)):
        return '04'
    array_out = []
    # Hace la operación indicada con el elemento i de los arreglos de entrada.
    for i in range(len(array_1)):
        x = basic_ops(array_1[i], array_2[i], operator)
        # Si basic_ops retorna un código de error, la función retorna ese mimso
        if ((x == '01') | (x == '02') | (x == '03')):
            return x
        array_out.append(x)
    return array_out
