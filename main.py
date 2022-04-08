from apartado1 import *
from apartado2 import *
from apartado3 import *

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




