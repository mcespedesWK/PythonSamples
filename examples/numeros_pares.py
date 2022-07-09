# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:00:12 2022

@author: Mauro
"""

"""
UN programa que me diga si un numero es para o es impar
"""

print("Introduce un numero")

numero = int(input())

#Para saber si un numero es para o impar necesitamos utilizar el MODULO

#SI el nuemro que yo meta al dividirlo entre 2 el resultado es 0 quiere decir que es par.
if(numero % 2 == 0):
    print("el numero",numero,"es par")
else:
    print("El numero",numero,"es impar")