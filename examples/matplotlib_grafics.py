# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:34:51 2022

@author: Mauro
"""

import numpy as np
import matplotlib.pyplot as plt

# Voy a crear una grafica que me muestre los nombre y los pesos en un grafico

nombre = ["Maria","Jose","Juan","Carla","Manolo", "Mauro"]

#Aqui utilizo la libreria de numpy para generar numeros aleatorios 
#El eso minimo es 50 y elo maximo 100
peso = np.random.randint(50,100, size= len(nombre))


plt.bar(nombre,peso)

plt.ylabel('Peso')
plt.xlabel('Nombres')

plt.title('Peso en kilogramosde los usuarios')

plt.show()