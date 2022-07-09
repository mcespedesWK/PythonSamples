# -*- coding: utf-8 -*-
"""
@author: Mauro
"""

import logging

# Importo mis módulos
# Para practicar cree dos módulos diferentes 
from threat_1.Modulo_hebra_1 import Clase_hebra_1
from threat_2.Modulo_hebra_2 import Clase_hebra_2

# Importo mi modelo de concurrencia con un alias
from modelos.concurrencia import Ejemplo_concurrencia as ec 


class Main:
    
    def __init__(self):
        # Creamos un archivo para guardar los mensajes
        # Escojemos el nivel de mensajes que deseamos mostrar con la opcion LEVEL
        # FILEMODE  lo que hace es escojer si sobre escribirmos el fichero o agregamos informacion
        #logging.basicConfig(format="%(asctime)s %(message)s",filename= 'ejemplo.log', filemode='a', level= logging.DEBUG)
 
        logging.basicConfig(level=logging.DEBUG,
                            format="%(asctime)s %(message)s",
                            datefmt='%m-%d %H:%M',
                            filename= 'logs/logs.log',
                            filemode='a',
                            )
    # Este metodo se encarga de recojer la información por pantalla del usuario
    def user(self):
        print('+------------------------------------------------+')
        print('|       PARALELISMO Y CONCURRENCIA               |')
        print('+------------------------------------------------+')
        print('| ')
        print('| Vamos a trabajar con dos listas que se sumaran concurrentemente ')
        print('+------------------------------------------------+')
        print(' ')
        
        print('+--------------------------------+')
        print('|  Lista 1: Escoja 3 números     |')
        print('+--------------------------------+')
        print(' ')        
        # Recojo la información del usuario en una variable en forma de lista
        lista1 = [int(input(' Primer número: ')),int(input(' Segundo número: ')),int(input(' Tercer número: '))]
        print(' ')
        # Pregunto al usuario cuantas hebras desea utilizar en el proceso
        var1 = int(input('¿Cuántas hebras desea utilizar?: '))
        print()
        
        print('+--------------------------------+')
        print('|   Lista 2: Escoja 3 números    |')
        print('+--------------------------------+')
        print(' ')
        lista2 = [int(input(' Primer número: ')),int(input(' Segundo número: ')),int(input(' Tercer número: '))]
        print()
        # Pregunto al usuario cuantas hebras desea utilizar en el proceso
        var2 = int(input('¿Cuántas hebras desea utilizar?: '))
        print(' ')
        print('+------------------------------------------------+')
        print()
        
        # Regreso las dos listas que voy a trabajar con el número de hebras que se quiere crear
        return lista1, lista2, var1, var2
    
    
    def main(self):
        
        # Recojo los dos returns del método user
        lista1,lista2,var1,var2 = Main.user(self)
        
        try:
            # Recibo los resultados del modelo de concurrencia
            # Paso como parámetrso las listas y el número de hebras 
            # Esto me regresará dos resultados que los guardo en una variable
            total1, total2  = ec.main(lista1,lista2,var1, var2) 
            
        except Exception as err:           
            # Utilizo el loggin para guardar los errores
            logging.warning(err)
        else: 
            print()
            print('+--------------------------------+')
            print('|       RESULTADOS               |')
            print('+--------------------------------+')
            print()
            print('| LISTA 1:')
            print('| Hebras utilizadas: ', var1)
            print('| Tiempo de ejecución: '+ str("{0:.2f}".format(total1)) +' segundos')
            print('+--------------------------------------+')
            print()
            print('| LISTA 2:')
            print('| Hebras utilizadas: ', var2)
            print('| Tiempo de ejecución: '+ str("{0:.2f}".format(total2)) +' segundos')
            print('+---------------------------------------+')
            print()


# Creo el Objeto para interactuar con la clase
object_1 = Main()

# Ejecuto el método a traves del objeto
object_1.main()