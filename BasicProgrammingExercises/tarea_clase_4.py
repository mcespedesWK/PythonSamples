# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:10:56 2022

@author: Mauro
"""

# Creo una clase que pueda contener operaciones matemáticas
class Operaciones():
    # Utilizo el método INIT que funciona como constructor de esta clase
    # Cuando el objeto de la clase es llamado automáticamente ejecuta la función init
    # Gracias a INIT el objeto podrá  utilizar cualquier propiedad o atributo de cualquier metodo de la clase de manera más sencilla
    # __init__(self)
    # Es más fácil declarar los parámetros que la clase recibe, dentro del método self
    # A la hora de crear el objeto de la clase, se DEBEN de pasar los argumentos para la clase. 
    # En este caso recibo una lista como parámetro
    def __init__(self,lista):
        # Primero llamo al SELF para que pueda ejecutar el metodo INIT
        # Empiezo a asignar atributos y les asigno un valor
        # En este caso la lista que recibo la inicializo aqui para todos los metodos de esta clase.
        # Ahora con SELF puedo llamar la lista con cualquier metodo que cree dentro de esta clase, y no tengo que escribirlo individualmente como parámetro en cada método
        self.lista = lista
        self.name_suma = 'SUMA'
        self.name_resta = 'RESTA'
        self.name_producto = 'MULTIPLICACION'
        self.name_division = 'DIVISION'

    # Defino una función para la suma
    # Recibe como parámetro la variable SELF
    def suma(self):
        #inicializo un contador en cero para que guarde el resultado de las interacciones
        counter = 0
        #Por cada elemento en lista
        for element in self.lista:
            # Ahora contador va a ser lo que había en la variable de contador más el número en la posición acutal dentro de la lista
            counter += element
        # Regreso información sobre el nombre de la función, los elementos de la lista y el resultado
        # El nombre de la operación y la lista los que definí en el metodo __INIT__ , entonces solo utilizo SELF para llamarlos
        return print('| El resultado de la ',self.name_suma,' de ', lista,'es: ', counter)
     
    # Defino una función para la resta 
    # Recibe como parámetro la variable SELF       
    def resta(self):
        #return [lista[i - 1] - lista[i] for i in range(1,len(lista))]
        # Inicializo una variable que me guarde el resultado
        # Inicializo la variable con el índice[0]
        resultado = self.lista[0]
        # Como inicialicé la variable RESULTADO en el indice 0, ahora recorro la lista desde el indice 1 hasta la longitud de la lista, osea el final de la lista
        for i in range(1,len(self.lista)):
            # El resultado es lo que tenía almacenado en la variable RESULTADO - la posición actual que recorro en la lista.
            resultado -= self.lista[i] 
        # Regreso información sobre el nombre de la función, los elementos de la lista y el resultado
        # El nombre de la operación y la lista los que definí en el metodo __INIT__ , entonces solo utilizo SELF para llamarlos
        return print('| El resultado de la ',self.name_resta,' de ', lista,'es: ', resultado)
    
    def producto(self):
        # Aqui inicializo la variable del resultado con 1
        # No la puedo incializar en cero porque cualquier numero multiplicado por cero da cero
        resultado = 1
        # Recorro la lista
        for i in self.lista:
            resultado *= i
        # Regreso información sobre el nombre de la función, los elementos de la lista y el resultado
        # El nombre de la operación y la lista los que definí en el metodo __INIT__ , entonces solo utilizo SELF para llamarlos
        return print('| El resultado de la ',self.name_producto,' de ', lista,'es: ', resultado)
    
    def dividir(self):
        # Aqui inicializo la variable con el índice 0 para que sea el número por el que dividimos en la primera vuelta
        resultado = self.lista[0]
        # Pero entonces ahora debo de recorrer el búcle FOR desde la posición 1 hasta el final de la lista
        for i in range(1,len(self.lista)):
            # Aquí puedo mostrar o no decimales ene lresultado
            resultado //= self.lista[i]
        # Regreso información sobre el nombre de la función, los elementos de la lista y el resultado
        # El nombre de la operación y la lista los que definí en el metodo __INIT__ , entonces solo utilizo SELF para llamarlos
        return print('| El resultado de la ',self.name_division,' de ', lista,'es: ', resultado)
                   
# Como tengo inicializado el metodo INIT y declaro que recibo una variable  LISTA
# Entonces a la hora de crear el objeto debo inicializar la variables que le envio a la clase
# En este caso es una lista con  valores introducidos por pantalla

print()
print('+------------------------------------+')
print('|             CALCULADORA            |')
print('+------------------------------------+')
lista = (int(input("| Valor de x: ")),int(input("| Valor de y: ")),int(input("| Valor de z: ")))

# Creo el objeto de la clase Operaciones y le paso como parámetro la lista que creé
calculadora = Operaciones(lista)

# Solicitamos al usuario que indique el tipo de operación
print()
print('+------------------------------------+')
print('| ¿ QUE OPERACION DESEA REALIZAR?    |')
print('+------------------------------------+')
print('+-----------------------------------------------------------+')
print('| 1-> SUMA |','2-> RESTA |',' 3-> MULTIPLICACION |','4-> DIVISION |: ')
print('+-----------------------------------------------------------+')

operacion = (int(input('Seleccione una operación: ')))

# Utilizo el try para controlar los errores de mi programa
# Intento ejecutar los métodos bajo el try
print('+------------------------------------+')
print('|              RESULTADO             |')
print('+------------------------------------+')
try:
    if operacion == 1:
        print('+----------------------------------------------------+')
        calculadora.suma()
        print('+----------------------------------------------------+')
    elif operacion == 2:
        print('+----------------------------------------------------+')
        calculadora.resta()
        print('+----------------------------------------------------+')
    elif operacion == 3:
        print('+----------------------------------------------------+')
        calculadora.producto()
        print('+----------------------------------------------------+')
    elif operacion == 4:
        print('+----------------------------------------------------+')
        calculadora.dividir()
        print('+----------------------------------------------------+')
    else:
        # Si el usuario ingresa otro número que no sea uno de los indicados
        # Arrojará la excepcion de tipo ValueError y este mensaje
        raise ValueError('Ha introducido un número incorrecto')
# Si el bloque de try no se puedo ejecutar aqui veo el tipo de excepcion 
# Si no conozco el  tipo de error puedo utilizar la clase general de Exception
except Exception as err:
    print('+-------------------------------------------------------------+')
    print('| Algo ha salido mal!!!: ', err, '|')
    print('+-------------------------------------------------------------+')
    

