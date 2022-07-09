from tkinter import *

# Para poder utilizar tabs
from tkinter import ttk
# Esto es para mostrar po up messages
from tkinter import messagebox
# Para trabajar con imagenes
from PIL import Image,ImageTk

# Este es el modelo que cree para realizar las predicciones
from models.classifier import Classifier as pred

# Import mi modelo para trabajar con graficas
from models.graphs import Graphs as gp

window = Tk()

window.geometry("350x350")
window.title("Iris app")
#########################
#    funtion_Pred      #
#########################
def function_pred():
    # Recibo por parametro los datso ingresados y lso asigno a una variable
    sw = e1.get()
    sl = e2.get()
    pw = e3.get()
    pl = e4.get()
    #--------------------------·
    #-- INYECTO datos
    #--------------------------·
    # convierto los datos en una lista para inyectarlo en la funcion
    # como un X_test una vez que el modelo esta entrenado
    testData = [[sl, sw, pl, pw]]

    # Llamo a mi metodo de desicionclassifier en el modelo de classifier
    # Obtengo las valieables para entrenar mi MODELO
    # Llamo directamente porque setup, trainig  los  llamo dentro del metodo
    X, Y = pred.setUp()
    X_train, X_test, y_train, y_test = pred.training(X,Y)
    #--------------------------·
    #-- CAMBIO lo datos por el INPUT que recibo del usuario
    #--------------------------·
    # Entonces voy a inyectar estos datos con todos los demas dentro del algoritmo.
    X_test = testData
    # Guardo la prediccion en una variable
    prediccion = pred.desicionClassifier(X_train, X_test, y_train, y_test)
     # Como tengo el eje Y  convertido en numeros lo debo de pasar a string
     # COn un bucle if analizo el retorno de la funcion
     #---> SETOSA
    if prediccion == 0:
        #Guardo en una variable el string que quiero usar
        result = 'Setosa'
        # Abrimos la imagen de SETOSA utilizando la libreria de imagenes que importamos
        image = ImageTk.PhotoImage(Image.open("img/setosa.png"))
        #---- GOOD STUFF ----
        # COn el config rellenamos la variables en la funcion principal
        # La las habiamos declarado vacias en el label
        # Aqui es donde les asignamos los valores con lo que obtengamos de la funcion
        lbl.config(text = "El tipo de especie es: "+result, image = image)
        # Llamo a la clase messaggebox de tkinter y muestro el resultado
        messagebox.showinfo('PREDICCION',' Según las caracteristicas es una SETOSA')
    #---> VERSICOLOR
    elif prediccion == 1:
        result = 'Versicolor'
        image = ImageTk.PhotoImage(Image.open("img/versicolor.png"))
        #---- GOOD STUFF ----
        lbl.config(text = "El tipo de especie es: "+result, image = image)
        # Llamo a la clase messaggebox de tkinter
        messagebox.showinfo('PREDICCION',' Según las caracteristicas es una VERSICOLOR')
    #---> VIRGINICA
    elif prediccion == 2:
        result = 'Virginica'
        image = ImageTk.PhotoImage(Image.open("img/virginica.png"))
        #---- GOOD STUFF ----
        lbl.config(text = "El tipo de especie es: "+result, image = image)
        # Llamo a la clase messaggebox de tkinter
        messagebox.showinfo('PREDICCION',' Según las caracteristicas es una VIRGINICA')

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def function_grafics():
    gp.species()

def _quit():
    window.quit()
    window.destroy()

#Aqui creamos el sistema de control de los tabs
tab_control = ttk.Notebook(window)
# Creamos tabs para cada cosa
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# Escribimos el nombre que va a llevar el tab
tab_control.add(tab1, text='Prediction')
tab_control.add(tab2, text='Graphs')


#----------------------------------
#   Agrego contenido a los tabs
#-----------------------------------
# Agregamos contenido a cada tab

                    ################
                    #    TAB 1
                    ################
#------------SET-LABELS---------------------------
# Primero divido la pantalla den Labels
labelTop = Label(tab1, fg="white", font="Sans 30")
labelTop.config(bg = "white")
labelTop.pack(fill= BOTH, side=TOP, pady = 5, padx = 5)

labelLeft = Label(tab1, fg="white", font="Sans 30")
labelLeft.pack(side=LEFT, pady = 5, padx = 5)

labelRight = Label(tab1, fg="white", font="Sans 30")
labelRight.pack(side=RIGHT, pady = 5, padx = 5)

#------------- SET TITLE ------------------------------
# Asigno un titulo a el tab
nombre= Label(labelTop, text = "Ingresa los datos para tu predicción",font=('Helvetica', '25','bold'),bg = '#7d625e', fg = 'white')
# Le digo que me ocupe todo el espacio en el eje X
nombre.pack(fill=X, side=TOP, pady = 1, padx = 1)
# Utilizo el label derecho para alinear los botones y entradas ahi
# La idea es desplegar el resultado en el label izquierdo

#--------DATOS y ENTRADAS ---------
Label(labelRight, text="Sepal width", font=('Helvetica', '20', 'bold')).grid(row=2,column=0)
Label(labelRight, text="Sepal length",font=('Helvetica', '20', 'bold')).grid(row=3,column=0)
Label(labelRight, text="Petal width",font=('Helvetica', '20', 'bold')).grid(row=4,column=0)
Label(labelRight, text="Petal length", font=('Helvetica', '20', 'bold')).grid(row=5,column=0)

# Entries
e1 = Entry(labelRight,width=10,  font=('arial', 16, 'bold'))
e1.insert(0, "")
# Esto es para que tenga un estilo con profundidad
e1.config(bd=8, relief=SUNKEN)
e1.grid(row=2, column=1)

e2 = Entry(labelRight,width=10, font=('arial', 16, 'bold'))
e2.insert(0, "")
# Esto es para que tenga un estilo con profundidad
e2.config(bd=8, relief=SUNKEN)
e2.grid(row=3, column=1)

e3 = Entry(labelRight,width=10, font=('arial', 16, 'bold'))
e3.insert(0, "")
# Esto es para que tenga un estilo con profundidad
e3.config(bd=8, relief=SUNKEN)
e3.grid(row=4, column=1)

e4 = Entry(labelRight,width=10, font=('arial', 16, 'bold'))
e4.insert(0, "")
# Esto es para que tenga un estilo con profundidad
e4.config(bd=8, relief=SUNKEN)
e4.grid(row=5, column=1)

# Este ees el boton que me llama a la funcion que muestra los datos
Button(labelRight,text="SHOW",bg = '#458a39', fg = 'white', command=function_pred, font=('Helvetica', '30'),relief=RAISED).grid(row=8,column=1)

Button(labelRight, text = "Quit", bg = 'red',fg = 'white', command = quit, font=('Helvetica', '30'), relief=RAISED).grid(row=10,column=1)

lbl = Label(labelLeft, text = "", font=('Helvetica', '30'), image = "",relief=RAISED)
lbl.pack()

                    ################
                    #    TAB 2
                    ################
# Utilizo la ventana del taba para que me muestre la info solo ahi
Label(tab2, text="Selecciona el tipo de grafico", font=('Helvetica', '30')).grid(row=1,column=0)
Button(tab2,text="Gráficas", command=function_grafics).grid(row=7,column=0)


###############################################
############################################3333
tab_control.pack(expand=1, fill='both')

window.mainloop()
