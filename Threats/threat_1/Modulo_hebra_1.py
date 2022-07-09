# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:14:11 2022

@author: Mauro
"""
# Sleep nos permite detener un proceso por un tiempo
# perf_counter nos permite contabilizar el timepo que dura en ejecutarse una funcion
from time import sleep, perf_counter

class Clase_hebra_1:
    
    # Recibo dos parámetros para poder trabajar la función
    # En este caso es una lista de números para sumar
    def func_hebra_1(lista1):
        #------------------------------------------------------
        #----------- INICIO COUNTER----------------------------
        # Esto nos dira el instante de tiempo cuando llamamos a la funcion
        tiempo_inicial = perf_counter()
        
        counter = 0
        for i in lista1:
            counter+= i   
            
        print('Este es el resultado de la suma de la LISTA-1: ',counter)
        print()
        
        # Todo se lee haci abajo 
        # Entonces esperamos que terminen y medimos el tiempo
        tiempo_final = perf_counter()
        #---------------FINAL COUNTER ---------------------------
        # -------------------------------------------------------
        
        t1 = tiempo_final-tiempo_inicial
        
        # Enviamos estos valores para poder mediar cunato dura la funcion 
        #cuando no se utilizan hebras
        return t1