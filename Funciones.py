#Función: realiza 4 operaciones distintas con dos operandos(+,-,&,|)
#Entrada: dos enteros entre -127 y 127 y un indicación de operación del 0 al 3
#Salida: Retorna el resultado de la operación
def basic_ops(num_1,num_2,operator):

    if  (operator == 0) : 
        return num_1 + num_2

    if  (operator == 1) : 
        return num_1 - num_2
    if  (operator == 2) : 
        return num_1 & num_2
    if   (operator == 3) : 
        return num_1 | num_2
        
 

#VERIFICACION DE DATOS DE ENTRADA ---------------------------------------------


try:
     num_1 = int(input('Operando 1: ')) #Pide el primer operador entero   
except:
    print('Debe ser entero') #Si no es entero envía codigo de error y termina programa
    exit(1)

try: 
    num_2 = int(input('Operando 2: '))    #Pide el segundo operador entero 
except:
    print('Debe ser entero')  #Si no es entero envía codigo de error y termina programa
    exit(1)

#Verifica que sea un entero entre -127 y 127, sino termina el programa
if (num_1 | num_2 < 127):
    if (num_1 | num_2 < -127):
        print('Operandos deben estar entre -127 y 127')
        exit(1)
else:
    print ('Operandos deben estar entre -127 y 127')
    exit(1)

 #Verifica el ingreso de operación que se entero y no menor a 0 ni mayor a 3   
try:
    operator = int(input('Operación: '))
except:
    print("Debe ser un valor entero entre 0 y 3")
    exit(1)
        
if( (operator > 3) | (operator < 0) ):
    print("Debe ser un valor entero entre 0 y 3")
    exit(1) 
   

#Se llama e imprime el valor que retorna la función 
print (basic_ops(num_1,num_2,operator))