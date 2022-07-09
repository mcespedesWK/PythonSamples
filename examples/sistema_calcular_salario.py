# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:06:32 2022

@author: Mauro
"""

"""
Haga un programa que calcule la nomina de un empleado de una empresa.

El sueldo bruto se calcula como:
    sueldo_bruto = base+complementos
    
- EL sueldo base será de 700 euros.
- EL complemento será de 400 euros si es un directivo y de 200 si no lo es

El sueldo neto se calcula aplicando un descuento en función del sueldo bruto. 
SI el sueldo bruto es inferiror a 100 euros, el descuento de IRPF es del 15% mientras que si en mayor el descuento 
será del 18%
"""

print("Ingrese el sueldo base")
base = float(input())

print("Es usted directivo? y/n")
directivo = input()


complemento = 200

if (directivo == 'y'):
    complemento = 400

sueldo_bruto = base + complemento

print("El sueldo bruto es de:", sueldo_bruto)

sueldo_neto = 0
if(sueldo_bruto <= 1000):
    sueldo_neto = sueldo_bruto - ((sueldo_bruto/100)*15)
else:
    sueldo_neto = sueldo_bruto -((sueldo_bruto/100)*18)
    
print("El sueldo neto es de :",sueldo_neto)
    
