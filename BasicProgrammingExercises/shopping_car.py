# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:23:08 2022

@author: Mauro
"""

import yaml
import tkinter

class Supermercado:
    
    def __init__(self):
        self.carne = 'C'
        self.helado = 'H'
        self.pasta = 'P'
        self.refresco = 'R'
        self.test = 'T'
        self.verdura = 'V'
        
    def car(self):
        pass  
    def stock(self):
        pass
    def prices(self):
        pass
    def pay(self):
        pass
    def screen(self):
        cathegory = {
                'C. Carnes': {'Pollo': 1,
                              'Cerdo':2            
                    },
                'P. Pastas':5,
                'V. Verduras': 6,
                'R. Refrescos':7,
                'H. Helados':8,
                'T. Test':{'1':1,'2':2,'3':3}
            }

        with open("catherory_products.yaml", 'w') as yamlfile:
            
            # COn el DUMP escribimos información en un archivo YAML
            data = yaml.dump(cathegory, yamlfile)
            #print("Write successful")

        
        print('+-------------------------------------------+')
        print('|        Welcome to the super market        |')
        print('+-------------------------------------------+')
       
        with open("catherory_products.yaml", "r") as cat:
            # Converts yaml document to python object
            data = yaml.safe_load(cat)
            #data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            #print("Read successful")
                      
            for i,j  in data.items():
                print('|', i)
                
        print('+-------------------------------------------+')
        cat =  input('| Seleccione la categoría de producto: ')    
        print('+-------------------------------------------+') 
        
        if cat == self.carne:
            for i,j in data.items():
                if i == 'C. Carnes':
                    
                    for r in j:
                        print(r)
                else:
                    pass
                
        elif cat == self.verdura:
            for i,j in data.items():
                if i == 'V. Verdura':
                    print(j)
                else:
                    pass
        elif cat == self.helado:
            for i,j in data.items():
                if i == 'H. Helado':
                    print(j)
                else:
                    pass
        elif cat == self.pasta:
            for i,j in data.items():
                if i == 'P. Pasta':
                    print(j)
                else:
                    pass
        elif cat == self.refresco:
            for i,j in data.items():
                if i == 'R. Refresco':
                    print(j)
                else:
                    pass
        elif cat == self.test:
            for i,j in data.items():
                if i == 'T. Test':
                    for r in j :
                        print(j[r])
                else:
                    pass
        
         

pantalla = Supermercado()

print(pantalla.screen())

