# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:17:10 2022

@author: Mauro
"""

#Con esta clase que hereda de Exceptions, puedo crear mis propias excepcciones
class misExcepciones(Exception):
    def __init__(self,valor):
        self.valorError = valor

'''
En este caso no voy a aceptar números negativos, entonces creo una excepcion para que salte cuando
alguien ingresa un número negativo.
'''


    
    
def ops(x,y):
    try:
        #Creo la condición para que evalúe si tira la excepción o no
        if x < 0 or y < 0:
            #Raise me sirve para lanzar mi propio error
            raise misExcepciones()
        else:
            suma = x+y
            resta = x-y
            print('+------------------------+')
            print('| Resultado de la suma:')
            print('|',x,"+",y,"= ",suma)
            print('| Resultado de la resta:')
            print('|',x,"-",y,"= ",resta)
            print('+------------------------+')
            print()
    #Ahora lanzo mi excepcion
    except misExcepciones:
        print('+------------------------------------------------------------------------+')
        print("| No se puede ejecutar esta acción porque uno de los números es negativo |")
        print('+------------------------------------------------------------------------+')
        
print(ops(int(input("Por favor ingrese un número: ")),int(input("Ahora ingrese otro número: "))))


#--------------------------------------------------------------------------#
#       Función con un parametro predefinido
#--------------------------------------------------------------------------#
'''
En este ejemplo defino el parametro y=10
El usuario escribe el valor de x para lograr la operacion

'''
def opsPre(x,y=10):

        suma = x+y
        resta = x-y
        
        print('En este ejemplo utilizo una variable predefinida y=10 ')
        print(x,"+",y,": ",suma)
        print(x,"-",y,": ",resta)
        
print('+--------------------------------+')
print("| Uso de parámetros predefinidos |")
print('+--------------------------------+')
print()

print(opsPre(int(input('Porfavor ingrese un número:'))))
