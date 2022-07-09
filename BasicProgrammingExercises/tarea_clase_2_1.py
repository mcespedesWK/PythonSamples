# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 18:51:58 2022

@author: Mauro
"""
#Solicito un número al usuario por pantalla
var = int(input("Por favor escriba un número entero: "))
print('+---+')
# var+1 para que incluya el último número
for i in range(0,var+1):
    #Si es menor o igual a var:
    if i <= var:
        print('|',i,'|')
    else:
        #Si es otra cosa termina el programa
        break

print('+---+')
print('+-----------------------+')
print('| Datos del diccionario |')
print('+-----------------------+')

#Creo un diccionario con valores cualquiera
#Un diccionario se compone de KEY:VALUE
dic = {'Nombre':'Mauro','Apellido':'Céspedes','Curso':'Progrmación Avanzada en Python',
       'Máster':['Python','Machine Learning','Hacking','Big Data'],'Edición':6,
       'Tema':'Diccionarios','Mensaje':'Esta es la tarea de la lección # 2'}

# El búcle for recorre el diccionario usando KEY
for key in dic:
    print('|',key, "---->",dic[key])