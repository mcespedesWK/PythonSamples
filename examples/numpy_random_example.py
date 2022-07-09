# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:25:25 2022

@author: Mauro
"""

import numpy as np

#Quiero que me genere numeros aleatorios hasta 20. COn el otro parametro le indico que me genere 50 de esos numeros.
v = np.random.randint(20, size = 50)
print("Los numeros aleatorios son:",v)

# para mostrar si los numeor son para a impar utilizo un blucle for

for i in v:
    if(i % 2 == 0):
        print (i, "es par")
    else:
        print (i, "es impar")