# -*- coding: utf-8 -*-
"""
@author: Mauro
"""

# Importo mis dos módulos en donde tengo los métodos que deseo ejecutar
from threat_1.Modulo_hebra_1 import Clase_hebra_1 as ch1
from threat_2.Modulo_hebra_2 import Clase_hebra_2 as ch2

# Sleep nos permite detener un proceso por un tiempo
# perf_counter nos permite contabilizar el timepo que dura en ejecutarse una funcion
from time import sleep, perf_counter

from threading import Thread


class Ejemplo_concurrencia:
    

    #------------------------------------
    #        CONCURRENCIA
    #------------------------------------
    # Rebibo las dos listas y el numero de threats 
    def main(lista1,lista2,var1,var2):
        
        # Aqui lo importante es crear tantos Theats como podamos
        # para sacarle el mayor provecho a los CORES
        
                        #------------------------------------
                        #           Lista 1
                        #------------------------------------
        #-------------------- START TIME LISTA 1 -----------------------
        # Esto nos dira el instante de tiempo cuando llamamos a la funcion
        time1 = perf_counter()
        
        #------------------------------------
        #       CREAR THREATS
        #------------------------------------
        # Me guarda la cantidad de threats que deseo crear
        threats1 = []

        # Utilizo un bucle for para generar los threats
        # Guardo cada threat en una lista
        # Aqui los creo y los ejecuto y enel siguiente les agrego el join
        for n in range(var1):
        #--->
        #--->
        #--->
            # Creo el Threat pero con un argumento
            # Que es el de  la posicion actual
            # SOLO acepta TUPLAS
            # Pero cuando sea solo un valor lo ponemos más una COMA dejando la segunda posicion vacía
            # Cuando son más parametro solo se agregan sin problema
            t= Thread(target= ch1.func_hebra_1(lista1),args=(n,))
            
            # Primero agrego la hebra a la lista
            threats1.append(t)
            
            # Una vez que tengamos creados y asignados los threads los tenemos que lanzar
            # Se inician con la funcion start
            t.start()
        
        # Ahora nos aseguramos que los procesos han terminado
        # COn el join esperaremos que la hbra haya terminado su trabajo
        # Que la hebra haya terminado la tarea que se le ha encomendado
        # Si no ponemos el JOIN estamos midiendo cunado se inicial la funcion 
        # Pero no se contabiliza el timepo en que termina, entonces no seria el tiempo real
        # UTILIZARLO para medir los resultados de las diferentes hebras
        # JOIN es como un semáforo en rojo que se pone en verde cuando la hebra termina su ejecucion
        # Ejecucion termina cuando sale de la funcion que le pasamos como parametro
        # Ahora esperamos que terminen de inicializarse cada hebra
        # Ahora recorro la lista con las hebras y asigno el JOIN
        for i in threats1:
            t.join()
        
        # Todo se lee haci abajo 
        # ENtonces esperamos que terminen y medimos el tiempo
        time1_final = perf_counter()
        #-------------------- END TIME LISTA 1 -----------------------
        
        total1 = time1_final-time1
        
        
                        #------------------------------------
                        #           Lista 2
                        #------------------------------------
        #-------------------- START TIME LISTA 2 -----------------------
        # Esto nos dira el instante de tiempo cuando llamamos a la funcion
        time2 = perf_counter()
        
        #------------------------------------
        #       CREAR THREATS
        #------------------------------------
        # Me guarda la cantidad de threats que deseo crear
        threats2 = []

        # Utilizo un bucle for para generar los threats
        # Guardo cada threat en una lista
        # Aqui los creo y los ejecuto y enel siguiente les agrego el join
        for n in range(var2):
        #--->
        #--->
        #--->
            # Creo el Threat pero con un argumento
            # Que es el de  la posicion actual
            # SOLO acepta TUPLAS
            # Pero cuando sea solo un valor lo ponemos más una COMA dejando la segunda posicion vacía
            # Cuando son más parametro solo se agregan sin problema
            t= Thread(target= ch2.func_hebra_2(lista2),args=(n,))
            
            # Primero agrego la hebra a la lista
            threats2.append(t)
            
            # Una vez que tengamos creados y asignados los threads los tenemos que lanzar
            # Se inician con la funcion start
            t.start()
        
        for i in threats1:
            t.join()
        
        # Todo se lee haci abajo 
        # ENtonces esperamos que terminen y medimos el tiempo
        time2_final = perf_counter()
        #-------------------- END TIME LISTA 2 -----------------------      
        total2 = time2_final - time2
        

        # Regreso ambos resultados para mostrarlos desde el menu principal
        return total1, total2
        
    