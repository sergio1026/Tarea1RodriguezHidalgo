#Función: realiza 4 operaciones distintas con dos operandos(+,-,&,|)
#Entrada: dos enteros entre -127 y 127 y un indicación de operación del 0 al 3
#Salida: Retorna el resultado de la operación
def basic_ops(num_1,num_2,operator):

    if (type(num_1)!=int):
        return 'Operandos deben ser enteros'

    if (type(num_2)!=int):
        return 'Operandos deben ser enteros'

    #Verifica que sea un entero entre -127 y 127, sino termina el programa  
    if ((num_1 | num_2 > 127) | (num_1 | num_2 < -127)):
        return 'Operandos deben estar entre -127 y 127'

    #Verifica el ingreso de operación que se entero y no menor a 0 ni mayor a 3   
    if (type(operator)!=int):
        return 'Debe ser un valor entero entre 0 y 3'

    if( (operator > 3) | (operator < 0) ):
        return 'Debe ser un valor entero entre 0 y 3'
    

    if  (operator == 0) : 
        return num_1 + num_2
    if  (operator == 1) : 
        return num_1 - num_2
    if  (operator == 2) : 
        return num_1 & num_2
    if   (operator == 3) : 
        return num_1 | num_2



def array_ops(array_1,array_2,operator):
    for i in range (len(array_1)):
        list fila
        for j in range(len(array_1[i])):
            fila.append(basic_ops(array_1[i][j],array_2[i][j],operator))
        array_out.append(fila)
    return array_out
        

#Se llama e imprime el valor que retorna la función 
print(basic_ops(2,1,0))

array_ops([[1,2],[1,2]],[[1,2],[1,2]],0)