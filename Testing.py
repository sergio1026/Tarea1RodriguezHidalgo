# Importa las funciones a testear y randint para generar enteros al azar
from Funciones import basic_ops
from Funciones import array_ops
from random import randint


# Función: Prueba la función basic_ops con generados al azar
def test_basic_ops():
    # Genera dos enteros entre -127 y 127
    x1 = randint(-127, 127)
    x2 = randint(-127, 127)
    # Utiliza assert para verificar el valor dado por la función
    assert(basic_ops(x1, x2, 0) == x1 + x2)
    assert(basic_ops(x1, x2, 1) == x1 - x2)
    assert(basic_ops(x1, x2, 2) == x1 & x2)
    assert(basic_ops(x1, x2, 3) == x1 | x2)


# Función: Prueba el error de que los operandos no sean int
def test_error01_basic_ops():
    # Código de error '01'
    assert(basic_ops('string1', 'string2', 0) == '01')  # Operando tipo string
    assert(basic_ops(1.2, 3.454565, 0) == '01')  # Operando con decimales


# Función: Prueba el error de que los operandos no esten entre -127 y 127
def test_error02_basic_ops():
    # Código de error '02'
    assert(basic_ops(128, 0, 0) == '02')  # Operando mayor a 127
    assert(basic_ops(0, -128, 0) == '02')  # Operando menor a -127


# Función: Prueba el error de que el operador no sea entero entre 0 y 3
def test_error03_basic_ops():
    # Código de error '03'
    assert(basic_ops(0, 0, 'stringop') == '03')  # Operador no es int
    assert(basic_ops(0, 0, 4) == '03')  # Operador mayor que 3
    assert(basic_ops(0, 0, -1) == '03')  # Operador menor que 0


# Función: Prueba la función array_ops con valores al azar en los arrays
def test_array_ops():
    # Genera el tamaño de los arrays de prueba entre 2 y 20
    r = randint(2, 20)
    array_1 = []
    array_2 = []
    # Añade números random entre -127 y 127 a los arrays
    for i in range(r):
        x1 = randint(-127, 127)
        x2 = randint(-127, 127)
        array_1.append(x1)
        array_2.append(x2)
    # Crea arrays con los resultados esperados
    array_plus = []
    array_minus = []
    array_and = []
    array_or = []
    for i in range(r):
        array_plus.append(array_1[i] + array_2[i])
        array_minus.append(array_1[i] - array_2[i])
        array_and.append(array_1[i] & array_2[i])
        array_or.append(array_1[i] | array_2[i])
    # Utiliza assert para probar los resultados esperados de array_ops
    assert(array_ops(array_1, array_2, 0) == array_plus)
    assert(array_ops(array_1, array_2, 1) == array_minus)
    assert(array_ops(array_1, array_2, 2) == array_and)
    assert(array_ops(array_1, array_2, 3) == array_or)


# Función: Prueba el error de que los operandos no sean int
def test_error01_array_ops():
    # Código de error '01'
    # Operando tipo string:
    assert(array_ops([1, 'string1'], ['string2', 1], 0) == '01')
    # Operando con decimales:
    assert(array_ops([1, 5.241], [6.945525, 1], 0) == '01')


# Función: Prueba el error de que los operandos no esten entre -127 y 127
def test_error02_array_ops():
    # Código de error '02'
    # Operando mayor a 127:
    assert(array_ops([1, 300], [128, 1], 0) == '02')
    # Operando menor a -127:
    assert(array_ops([1, -1300], [-128, 1], 0) == '02')


# Función: Prueba el error de que el operador no sea entero entre 0 y 3
def test_error03_array_ops():
    # Código de error '03'
    # Operador no es int:
    assert(array_ops([1, 2, 3], [127, 126, 125], 'operator') == '03')
    # Operador mayor que 3:
    assert(array_ops([1, 2, 3], [127, 126, 125], 4) == '03')
    # Operador menor que 3:
    assert(array_ops([1, 2, 3], [127, 126, 125], -1) == '03')
