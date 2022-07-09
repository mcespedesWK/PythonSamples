# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:19:32 2022

@author: Mauro
"""

# Creo una función para imprimir en pantalla
# Recibe tres parámetros de entrada
def moldura(tema,lista,lista2):
    print('+-------------------------+')    
    if tema == 'listas':
        print('|          LISTAS         |')
        print('+-------------------------+')
        print('| Lista del 1-10: ')
        print('| ',lista)
        print('+-------------------------+')
        print('| Lista inversa del 10-0: ')
        print('| ',lista2)
        print('+-------------------------+')
    elif tema == 'diccionarios':
        print('|        DICCIONARIOS       |')
        print('+-------------------------+')
        print('| Los valores introducidos son:')
        print('| ',lista)
        temp = input('¿Desea modificar algún valor?: Y/N  ')
        
        counter = True
        if temp == 'Y':   
            while counter == True:
                modificar(lista,counter)
        else:
            counter = False
            agregar(lista)
            
            
def modificar(lista,counter):
    var = int(input('Indique el valor a modificar: '))
    for i in lista:
        if i == var:
            ind = lista.index(var)
            sust = int(input('¿Por qué valor deseas sustituir?: '))
            lista.remove(var)
            lista.insert(ind,sust)
            break
    print('| Ésta es la nueva lista: ')
    print('| ',lista) 
    
    
    
def agregar(lista):
    
    var = True   
    while var == True:
        var = input('Desea agregar más números?: Y/N')    
        if var  == 'Y':
            lista.append(int(input('¿Qué valor deseas añadir?: '))) 
            print(lista)
            agregar(lista)
        else:
            var = False
            print('Fin del programa')
        
# Primero inicializo una lista vacía
lista = []

# Este es un contandor para saber cuanto dura el bucle while
i= 0
# Mientras no se llegue a 10 continua
while i <= 10:
    # Y en cada vuelta adjunta el elemento de la posición en la que estamos
    lista.append(i)
    # Sumo la vuenta en el contador
    i +=1

# Creamos otra lista que almacene los números en orden invertido
lista_2 = []

# Utilizo la función range para recorrer la lista de atrás hacia adelante
# START será 10 la longitud de lal ista
# STOP será -1 para que me incluya el cero (10 9 8 7 6 5 4 3 2 1 0)
# STEP será de -1 para que valla en sentido contrario
for i in range(10,-1,-1):
    # Append a la nueva lista cada vuelta
    lista_2.append(i)
    
moldura('listas', lista, lista_2)

#------------------------
#       DICCIONARIO
#------------------------
print('+-----------------------------+')
print('| Ejercicio con diccionarios |')
print('+-----------------------------+')

# Pido al usuario cuatro valores por pantalla y los almaceno en una lsita
num = [int(input('Primer valor: ')),int(input('Segundo valor: ')), int(input('Tercer valor: ')),int(input('Cuarto valor: '))]

moldura('diccionarios',num,lista)