# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:50:04 2022

@author: Mauro
"""
# Lo primero que hago es utilizar las excepciones al importar los módulos
# Así puedo controlar los errores que surjan al importar

try:
    # Voy a utilizar dos formas de importar paquetes
    # Primero importo solo lo que necesito directamente de cada sub-package
    # En este caso importo los modulos de cada uno para utilizar sus funciones
    from package.sub_package1 import mod1,mod2
    from package.sub_package2 import mod3, mod4
    
    # Ahora utilizo directamente el import para llamar a un modulo que no pertenece a ningún sub-paquete
    # El modulo se encuetra en el mismo nivel que los sub-paquetes
    # Tambien quize practicar un poco el Alias
    import package.prueba as pb
# Utilizo la excepción específica para módulos
except ModuleNotFoundError as err:
    print('Opssss... Parece que hubo un error importando el paquete', err)
    
    
# Como ya tengo los modulos importados ahora solo llamo al modulo y la función dentro de él
# Llamo a la función 'to_print()' 
mod1.to_print()
# Imprimo la ruta en donde está ubicado el módulo
print(mod1.__file__)
# Imprimo en pantalla el nombre del módulo
print(mod1.__name__)
#----------------------------------------------------------
#----------------------------------------------------------
mod2.to_print()
# Imprimo la ruta en donde está ubicado el módulo
print(mod2.__file__)
# Imprimo en pantalla el nombre del módulo
print(mod2.__name__)
#----------------------------------------------------------
#----------------------------------------------------------
mod3.to_print()
# Imprimo la ruta en donde está ubicado el módulo
print(mod3.__file__)
# Imprimo en pantalla el nombre del módulo
print(mod3.__name__)
#----------------------------------------------------------
#----------------------------------------------------------
mod4.to_print()
# Imprimo la ruta en donde está ubicado el módulo
print(mod4.__file__)
# Imprimo en pantalla el nombre del módulo
print(mod4.__name__)
#----------------------------------------------------------
#----------------------------------------------------------
# En el caso del módulo prueba hago lo mismo y llamo a la función dentro del módulo
# Este módulo tiene más variables que no quiero que se ejecuten
# Entonces dentro del módulo utilizo un IF y la función __name__ para evitar que se ejecute ese bloque de código
# Solo se verá si el archivo del mismo módulo se está ejecutando.
print(pb.to_print())