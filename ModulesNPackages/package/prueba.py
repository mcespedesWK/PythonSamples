# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:50:04 2022

@author: Mauro
"""

def to_print():
    print('+-----------------------------------+')
    print('|           MODULO PRUEBA           |')
    print('+-----------------------------------+')
    print('| Esto es una prueba rápida ')
    
    

# En caso que tengamos otro código dentro del mismo mçodulo que no queremos que se ejecute cunado llamemos al módulo
# Para ello utilizamo la función __name__ y que el códgio solo se ejecute si se está ejecutando el archivo
variable = 7
if(__name__ == '__main__'): 
    suma = 5 + variable
    print(suma)
        