# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:57:15 2022

@author: Mauro
"""
# Defino una función par ala suma que pueda ser reutilizada
# Recibe como parámetro la variable lista
def suma(lista):
    #inicializo un contador en cero para que guarde el resultado de las interacciones
    counter = 0
    #Por cada elemento en lista
    for element in lista:
        # Ahora contador va a ser lo que había en la variable de contador más el número en la posición a cutal de la lista
        counter += element
    #Regreso counter
    return counter
 
# Defino una función para la resta que pueda ser reutilizada
# Recibe como parámetro la variable lista       
def resta(lista):
    
    
    #return [lista[i - 1] - lista[i] for i in range(1,len(lista))]
    
    #Inicializo una variable que me guarde el resultado
    #Inicializo la variable con el índice[0]
    resultado = lista[0]
    #Recorrer 'i' en un rango que comience de 1 hasta la longitud de la lista.
    for i in range(1,len(lista)):
        # El resultado es lo que tenía almacenado en la variable - la posición actual que recorro en la lista.
        resultado -= lista[i] 
    #Cuando termíno el bucle regreso el valor final de resultado   
    return resultado

# Esta funciçon lo único que hace es darle formato a los resultados
# Toma dos parametros que el usuario ingresa por pantalla
def molde(lista, seleccion):
    print()
    print('+------------------------------------+')
    print('|     Resultado de la operación      |')
    print('+------------------------------------+')
    
    if seleccion == 'S':
        print('| Ésta es una suma:')
        # Llamo a la función suma para que me arroje el resultado 
        print('| ',lista[0],'+',lista[1],'=', suma(lista))
        print('+------------------------------------+')
        
    elif seleccion == 'R':
        print('| Ésta es una resta:')
        # Llamo a la función suma para que me arroje el resultado 
        print('| ',lista[0],'-',lista[1],'=', resta(lista))
        print('+------------------------------------+')
    else:
        # Si el usuario ingresa otra cosa que no sea R o S se termina el prorama y arroja este mensaje:
        print('-',seleccion,'-',' no se reconoce como una operación. El programa termina ahora.')
            
    
#-----------------------------------------------
#   Solicitud de datos por pantalla
#-----------------------------------------------

# Creo ésta variable para repetir el búcle While mientras sea True
repetir = True
# Utilizo un while para que el ciclo se repita hasta que el usuario ingrese un valor correcto
while repetir == True:
    # Utilizo el try para controlar los errores de mi programa
    # Intento recojer los datos bajo el try
    try:
        #Genero un alista con dos valores que el usuario ingresa
        lista = [int(input('Dame un número: ')),int(input('Dame otro número: '))]
        # Solicito al usuario el tipo de operacion que desea realizar
        seleccion = input('¿Que operaión deseas hacer?: Escribe S para suma o R para resta  ')
    
    # Si el bloque de try no se puedo ejecutar aqui veo el tipo de excepcion 
    # Si no conozco el  tipo de error puedo utilizar la clase geneal de Exception
    except Exception as err :
        print(f"Hay un error de tipo: {err}")
    # ESi el bloque de try se pudo ejecutar , entonces ahora si llamo a la funcion de MOLDE
    # Le paso como parametros la informacion que obtuve dentro del bloque try.
    else: 
        # Una vez que se pueda ejecutar el bloque TRY cambiamos la variable a FALSE
        repetir = False
        # Aqui llamo a la funcion para que me imprima los resultados
        print(molde(lista, seleccion))
    

#------------------------------------------------------------------------------------------------- 
'''
PARAMETROS PREDEFINIDOS

Ahora utilizo un parametro predefinido dentro de una función
La función recibe dos parámetros, pero si solo se le envía uno la función utiliza un parametro predefinido
'''

# Si la función solo recibe un parámetro utilizará el parametro predefinido
def param(x, y=3):
    # Variable almacena resultado de la resta
    suma = x+y
    # Variable almacena resultado de la resta
    resta = x-y
    
    # Regreso los resultados de la suma y la resta en forma de diccionario
    return {'x + y ':suma, 'x - y ':resta}

print('+--------------------------------+')
print("| Uso de parámetros predefinidos |")
print('+--------------------------------+')

# Usuario ingresa valor por pantalla
x = int(input('Porfavor ingrese un número:'))

print('+--------------------------------+')
print("| Uso de parámetros predefinidos |")
print('+--------------------------------+')
print('| X = ', x)
print('| Y = 3')
print('|')
print('|',param(x))
print('+--------------------------------+')
