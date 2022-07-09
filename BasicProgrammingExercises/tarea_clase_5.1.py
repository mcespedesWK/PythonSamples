# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:19:32 2022

@author: Mauro
"""

# Lo primero es crear una clase que contenga todos los métodos que utilizaremos
class Ops:
    # Utilizo el método INIT que funciona como constructor de esta clase
    # Cuando el objeto de la clase es llamado automáticamente ejecuta la función init
    # Gracias a INIT el objeto podrá  utilizar cualquier propiedad o atributo de cualquier metodo de la clase de manera más sencilla
    # __init__(self)
    # Es más fácil declarar los parámetros que la clase recibe, dentro del método self
    # A la hora de crear el objeto de la clase, se DEBEN de pasar los argumentos para la clase. 
    # En este caso recibo 3 parámetros
    def __init__(self,name,lista, lista_2):
        self.lista = lista
        self.name = name
        self.lista_2 = lista_2
    
    def marco(self):
        # Hago una especie de Frame aprovechando la funcion print()
        print('+-------------------------+')
        # Si el self.name que recibi como parámetro  es igual a lista, entonces....
        if self.name == 'lista':
            print('|          LISTAS         |')
            print('+-------------------------+')
            print('| Lista del 1-10: ')
            print('------------------')
            print('| ',self.lista)
            print('+-------------------------+')
            print('| Lista inversa del 10-0: ')
            print('--------------------------')
            print('| ',self.lista_2)
            print('+-------------------------+')
            print()
            print()
        # Si self.name es igual a diccionarios ejecuto...
        elif self.name == 'diccionarios':
            print('+------------------------------+')
            print('| Los valores introducidos son:')
            print('+------------------------------+')           
            # Imprimo en pantalla los valores que el usuario ingresa
            
            for key in self.lista:
                value = self.lista.get(key)
                print("{} : {}".format(key, value))
            print('+------------------------------+')
            
            # Guardo los valores del diccionario en una variable
            var = self.lista
            # Ahora llamo al metodo de modificar la info en caso que se necesite alguna conrrección
            Ops.modificar(self,var)
        else:
            pass

    
    def agregar(self,var):
        # Creo ésta variable para repetir el búcle While mientras sea True
        counter = True
        # Utilizo un while para que el ciclo se repita hasta que el usuario desee salir
        while counter == True:
            # Utilizo el try para controlar los errores de mi programa
            # Intento recojer los datos bajo el try
            try:
                seleccion = input('Desea agregar más campos de información?: Y/N: ')    
                if seleccion  == 'Y':
                        var[(input('Ahora indique el nombre del campo: '))]= input('Primero ingrese el valor del nuevo campo: ') 
                else:
                    # Si el usuario ya no quiere ingresar más datos le solicitaré al usuario que ingrese una lista de profesiones
                    Ops.add_list(self,var)
                    break
            # Si el bloque de try no se puedo ejecutar aqui veo el tipo de excepcion 
            # Si no conozco el  tipo de error puedo utilizar la clase geneal de Exception
            except Exception as err :
                print(f"Opppsss... Parece que hay un error de tipo: {err}")
            else: 
                # Una vez que se pueda ejecutar el bloque TRY cambiamos la variable a FALSE
                counter = False
                print('+-------------------------+')
                print('| Ésta es la nueva lista: ')
                print('+-------------------------+')
                print('| ',var)
                Ops.agregar(self, var)


    def modificar(self,var):
        # Creo ésta variable para repetir el búcle While mientras sea True
        counter = True
        # Utilizo un while para que el ciclo se repita hasta que el usuario desee salir
        while counter == True:
            # Utilizo el try para controlar los errores de mi programa
            # Intento recojer los datos bajo el try
            try:
                # Pregunto al usuario si desea
                temp = input('¿Desea modificar algún campo?: Y/N  ')
                # Si la respuesta es si entonces ejecuto...
                if temp == 'Y': 
                    # Le solicito al usuario la informacion dentro del diccionario
                    valor = input('Indique nombre del campo: ')
                    
                    # SI el valor realmente existe dentro de la lista.
                    if valor in var:
                        sust = input('¿Por qué valor deseas sustituir?: ')
                        var.update({valor:sust})
                        print('+-------------------------+')
                        print('| Ésta es la nueva lista: ')
                        print('+-------------------------+')
                        print('| ',var)
                        Ops.agregar(self,var)
                    else:
                        raise Exception()
                else:
                    Ops.agregar(self,var)
                    
                    
            # Si el bloque de try no se puedo ejecutar aqui veo el tipo de excepcion 
            # Si no conozco el  tipo de error puedo utilizar la clase geneal de Exception
            except Exception as err :
                print(f"Opppsss... Parece que hay un error de tipo: {err}")
            else:
                counter = False
            
    def add_list(self,var):
        # Creo ésta variable para repetir el búcle While mientras sea True
        counter = True
        # Utilizo un while para que el ciclo se repita hasta que el usuario desee salir
        while counter == True:
            # Utilizo el try para controlar los errores de mi programa
            # Intento recojer los datos bajo el try
            try:
                
                profesiones = {" Policia":1,'Bombero':2,'Electricista':3,'Carnicero':4,'Malabarista':5,'Deportista':6,'Vendedor':7,'Programador':8,'Pintor':9}
                # Pregunto al usuario si desea
                print(''' Gracias por la informácion. Tu registro está casi listo!!
                      Ahora solo necesito que de la siguiente lista de profesiones
                      escojas las tres que más se acerquen a tu perfil. Escribe el número de la opción.
                             ''')
                for key,value in profesiones.items():
                    print(value,'------>',key)
                
                opcion_list = [int(input('Cual es tu primera opción?: ')),int(input('Cuál es tu segunda opción?')),int(input('Cuál es tu última opción?'))]
                opcion_names = []
                for i in opcion_list:
                    for key,value in profesiones.items():     
                        if value == i:
                            opcion_names.append(key)
                        else:
                            pass                          
                
                print()
                var['Profesiones similares']= opcion_names
                print('+-------------------------+')
                print('| Ésta es su ficha: ')
                print('+-------------------------+')
                for key,value in var.items():    
                    print('|',key,' : ',value)
                print()
                break
       
            # Si el bloque de try no se puedo ejecutar aqui veo el tipo de excepcion 
            # Si no conozco el  tipo de error puedo utilizar la clase geneal de Exception
            except Exception as err :
                print(f"Opppsss... Parece que hay un error de tipo: {err}")
            else:
                print()
                print('Muchas gracias!')
                break
#--------------------
#------------------------------------------------------------------

                    #-----------------------#
                    #         LISTA         #
                    #-----------------------#

# Primero inicializo una lista vacía para almacenar los números
lista = []

# Este es un contandor para saber cuanto dura el bucle while
i= 0
# Mientras no se llegue a 10 continua
while i <= 10:
    # Y en cada vuelta adjunta el elemento de la posición en la que estamos
    lista.append(i)
    # Sumo la vuelta en el contador
    i +=1
#------------------------------------------------------------------
# Creamos otra lista que almacene los números en orden invertido
lista_2 = []

# Utilizo la función range para recorrer la lista de atrás hacia adelante
# START será 10 la longitud de la lista
# STOP será -1 para que me incluya el cero (10 9 8 7 6 5 4 3 2 1 0)
# STEP será de -1 para que valla en sentido contrario
for i in range(10,-1,-1):
    # Append a la nueva lista cada vuelta
    lista_2.append(i)
#------------------------------------------------------------------

# Creo un objeto de la clase Ops y le paso tres parámetros que los recibe el metodo INIT
listado = Ops('lista', lista, lista_2)

# Ahora llamo a un método de la clase y se lo asigno al objeto
# Se imprimirá e pantalla lo que el método indique
listado.marco()

#------------------------------------------------------------------

                    #-----------------------#
                    #       DICCIONARIO     #
                    #-----------------------#
#-----------------------------------------------
#   Solicitud de datos por pantalla
#-----------------------------------------------

# Creo ésta variable para repetir el búcle While mientras sea True
repetir = True
# Utilizo un while para que el ciclo se repita hasta que el usuario ingrese un valor correcto
while repetir == True:
    # Utilizo el try para controlar los errores de mi programa
    # Intento recojer los datos bajo el try
    try:
        print('+-----------------------------+')
        print('| Por favor ingrese sus datos:|')
        print('+-----------------------------+')
        # Pido al usuario cuatro valores por pantalla y los almaceno en un diccionario
        num = {'Nombre':(input('Nombre: ')),'Apellido':(input('Apellido: ')), 'Edad':(int(input('Edad: '))),'Peso':(float(input('Peso: ')))}  
    # Si el bloque de try no se puedo ejecutar aqui veo el tipo de excepcion 
    # Si no conozco el  tipo de error puedo utilizar la clase geneal de Exception
    except Exception as err :
        print(f"Oppppssss....hay un error de tipo: {err}. ¿Empezamos de nuevo?")
    # ESi el bloque de try se pudo ejecutar , entonces ahora si llamo a la funcion de MOLDE
    # Le paso como parametros la informacion que obtuve dentro del bloque try.
    else: 
        # Una vez que se pueda ejecutar el bloque TRY cambiamos la variable a FALSE
        repetir = False
        diccionario = Ops('diccionarios',num,lista)
        diccionario.marco()



