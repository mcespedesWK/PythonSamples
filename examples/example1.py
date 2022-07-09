# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Programa quie calcule el area de un círculo apartir del radio(leído por teclado)
area = pi*r**2
"""

# El cuadrado de un numero siempre se ecribe con  *
# E sla forma de elevar en Python

# Para poder utlilizar la libreria de Math tenemos que importarla
# En este ejemplo solo utilizaremos la funcion PI

#from math import *
from math import pi

print("Introduce el radio del circulo")
r = float(input())

#area = math.pi*r**2
area = pi*r**2

print("El area del circulo es:",area)