from apartado1 import *

class Calificaciones3():
    def __init__(self, archivo):
        self.archivo = archivo

    def creardiccionario(self):
        datos = pd.read_csv(self.archivo, header=0)
        
        parcial_1 = list(datos["Parcial1"])
        parcial_2 = list(datos["Parcial2"])
        asistencia = list(datos["Asistencia"])
        nombre = list(datos["Nombre"])
        examenpracticas = list(datos["OrdinarioPracticas"])

        for i in range(1,17):
            diccionario = {"Nota primer parcial {}".format(nombre[i]) : parcial_1[i] , "Nota segundo parcial {}".format(nombre[i]) : parcial_2[i] , "Asistencia" : asistencia[i], "Notafinal" : (parcial_1[i] * 0.3 + parcial_2[i] * 0.3 + examenpracticas[i] * 0,4)}

    def aprobados(self):
        datos = pd.read_csv(self.archivo, header=0)

        parcial_1 = list(datos["Parcial1"])
        parcial_2 = list(datos["Parcial2"])
        asistencia = list(datos["Asistencia"])
        nombre = list(datos["Nombre"])
        examenpracticas = list(datos["OrdinarioPracticas"])

        for i in range(1,17):
            if asistencia[i] >= 0.75 and parcial_1[i] > 4 and parcial_2[i] > 4 and examenpracticas[i] > 4 and (parcial_1[i] * 0.3 + parcial_2[i] * 0.3 + examenpracticas[i] * 0,4) > 5:
                print("{} Aprobado".format(nombre[i]))


        



csv = Calificaciones("calificaciones.csv")
csv.aprobados()