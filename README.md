# ARCHIVOS

El link al repositorio es el siguiente: https://github.com/Germiprogramer/ARCHIVOS.git

# Ejercicio1
    import pandas as pd

    class Calificaciones():
        def __init__(self, archivo):
            self.archivo = archivo

        def creardiccionario(self):
            datos = pd.read_csv(self.archivo, header=0)

            notas= []


            parcial_1 = list(datos["Parcial1"])
            parcial_2 = list(datos["Parcial2"])
            asistencia = list(datos["Asistencia"])
            nombre = list(datos["Nombre"])

            for i in range(1,17):
                diccionario = {"Nota primer parcial {}".format(nombre[i]) : parcial_1[i] , "Nota segundo parcial {}".format(nombre[i]) : parcial_2[i] , "Asistencia" : asistencia[i]}
                notas.append(diccionario)
            print(notas)


    csv = Calificaciones("calificaciones.csv")
    csv.creardiccionario()
 <img width="182" alt="2022-04-08 (4)" src="https://user-images.githubusercontent.com/91720991/162432961-72d2cb44-85aa-432e-b94f-b4268383c446.png">
   
# Ejercicio 2

    from apartado1 import *

    class Calificaciones2():
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

    csv = Calificaciones("calificaciones.csv")
    csv.creardiccionario()
<img width="182" alt="2022-04-08 (5)" src="https://user-images.githubusercontent.com/91720991/162432981-22b0a08e-fff2-43b2-8d00-feee7a60cb08.png">


# Ejercicio 3

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
<img width="190" alt="2022-04-08 (3)" src="https://user-images.githubusercontent.com/91720991/162432902-a01a8335-0ed6-4e85-9eab-584383a33807.png">

# MAIN

if __name__ == "__main__":
    print("Ejercicio 1")
    csv = Calificaciones("calificaciones.csv")
    csv.creardiccionario()
    print("Ejercicio 2")
    csv = Calificaciones2("calificaciones.csv")
    csv.creardiccionario()
    print("Ejercicio 3")
    csv = Calificaciones3("calificaciones.csv")
    csv.aprobados()
