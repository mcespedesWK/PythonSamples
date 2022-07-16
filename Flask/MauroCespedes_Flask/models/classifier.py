import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Lo primer es desidir si estamos antes un problema de:

    # 1- Regresión
    # 2- Clasificacion
    # 3- Clustering
#--------------------------------------#
# ---     1- DesicionClasifier     -----
#--------------------------------------#
# Para saber que libreria utilizar es necesario saber ante que problema nos enfrenteamos
# En este caso utilizamos un algoritmo de      ----> Clasificacion Multivariable <-------
# En donde la salida es de 0,1,2
from sklearn.tree import DecisionTreeClassifier
#--------------------------------------#
# ---   2- RandomForestClassifier  -----
#--------------------------------------#
from sklearn.ensemble import RandomForestClassifier

# Ahora importo la libreria de sklearn para crear mis SETs de Training y TEST
from sklearn.model_selection import train_test_split

# Ahora EVALUO EL MODELO
# Uso accuracy_Score pero hay otras

from sklearn.metrics import accuracy_score

class Classifier():

    def setUp(f):
        #The above function creates a dictionary with sheet names in the Excel files as
        #keys and dataframe as values. You can now access the dataframe with its sheet name.
        # Leo el archivo queme llega por request

        df = pd.read_excel(f,sheet_name=None)

        # Aqui obtenemos el numero de tabs que vienen en la hoja
        # Hacemos una lista para guardar el numero de get_sheet_names
        holder = []
        #--------------------------------------------------

        # Recorrermos el array por keys que son las tabs# Esto porque el archivo se guarda com dicccionario
        for i in df.keys():
            holder.append(i)
        #------------------------------------------------------
        table_class = "rwd-table"
        html = """<style> table {border-collapse: collapse; width: 100%; } th, td {text-align: left; padding: 8px; } tr:nth-child(even) {background-color: #f2f2f2;} </style>"""
        html += """
                <script>
                  window.console = window.console || function(t) {};
                </script>
                <script>
                  if (document.location.search.match(/type=embed/gi)) {
                    window.parent.postMessage("resize", "*");
                  }
                </script>"""
        return table_class, html, holder

"""
    def write_file():
        # Aqui unimos cada taba que viene en el reporte
        #Guardamos todo en un solo reporte para poder manipularlo.
        with pd.ExcelWriter('finalReport.xlsx', engine='xlsxwriter') as writer:
            for i in holder:
                # Hago las variables dinamicas
                df[i].to_excel(writer, sheet_name= i , index=False)
                df[i].to_html(i+".html")

                with open(i+".html") as file:
                    file = file.read()

                file = file.replace("<table ", "<table class=\"" + table_class + "\" ")

                with open(i+".html", "w") as file_to_write:
                    file_to_write.write(html + file)
                    #os.startfile(i+".html")
"""
