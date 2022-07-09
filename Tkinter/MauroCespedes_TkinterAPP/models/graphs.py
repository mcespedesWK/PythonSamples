import tkinter as tk
import pandas as pd
#--> Matplotlib libraries
#Libreiras necesarias para la visualizacion de datos
from  matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

class Graphs():

    def species():
        # Creamos la instancia de Tkinter y la llamamos raiz
        graf = tk.Tk()

        # Añadimos un titulo a la ventana
        graf.title("Embedding in Tk")

        # Leo el dataframe que deseo utilizar
        df = pd.read_csv("iris.csv")

        #------- CREAR FIGURA -------------
        # Aqui es la figura donde vamos a incorporar la grafica. Definimos el tamaño
        figura = Figure(figsize=(6,4))
        # Ahora tengo que seleccionar el valor dentro del data frame que deseo plotear
        # Esto es escojer la columna que deseo

        figura.add_subplot(111).plot(df.species)

        #--------- CREAR CANVAS ----------
        # Creamos el canvas en el cual pasamos la fugura que acabamos de crear
        # la vamos a insertar en ese canvas
        canvas = FigureCanvasTkAgg(figura,graf)
        # Le pedimos que nos lo dibuje
        canvas.draw()
        #
        canvas.get_tk_widget().pack()

        # Esto no es necesario si no se quiere
        # Permite interactuar con el canvas una vez desplegado
        toolbar = NavigationToolbar2Tk(canvas, graf)
        #Que se actualice con cualquier cambio
        toolbar.update()
        # Esto es para que nos cree el grafico.
        canvas.get_tk_widget().pack()
        tk.mainloop()


    def description():
        pass

    def count():
        pass
