import pandas as pd

class Calificaciones():
    def __init__(self, archivo):
        self.archivo = archivo

    def creardiccionario(self):
        datos = pd.read_csv(self.archivo, header=0)
        
        parcial_1 = list(datos["Parcial1"])
        parcial_2 = list(datos["Parcial2"])
        asistencia = list(datos["Asistencia"])
        nombre = list(datos["Nombre"])

        for i in range(1,17):
            diccionario = {"Nota primer parcial {}".format(nombre[i]) : parcial_1[i] , "Nota segundo parcial {}".format(nombre[i]) : parcial_2[i] , "Asistencia" : asistencia[i]}





csv = Calificaciones("calificaciones.csv")
csv.creardiccionario()
