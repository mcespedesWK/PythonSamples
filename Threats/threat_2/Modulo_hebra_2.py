# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:14:34 2022

@author: Mauro
"""
# Sleep nos permite detener un proceso por un tiempo
# perf_counter nos permite contabilizar el timepo que dura en ejecutarse una funcion
from time import sleep, perf_counter

class Clase_hebra_2:
   
    # Recibo dos parámetros para poder trabajar la función
    # En este caso es una lista de números para sumar
    def func_hebra_2(lista2):
        #------------------------------------------------------
        #----------- INICIO COUNTER----------------------------
        # Esto nos dira el instante de tiempo cuando llamamos a la funcion
        tiempo_inicial = perf_counter()
        
        counter = 0
        for i in lista2:
            counter+= i  
            
        print('Este es el resultado de la suma de la LISTA-2: ',counter)
        print()
        
        # Todo se lee haci abajo 
        # Entonces esperamos que terminen y medimos el tiempo
        tiempo_final = perf_counter()
        #---------------FINAL COUNTER ---------------------------
        # -------------------------------------------------------
        
        t2 = tiempo_final-tiempo_inicial
        # Enviamos estos valores para poder mediar cunato dura la funcion 
        #cuando no se utilizan hebras
        return t2