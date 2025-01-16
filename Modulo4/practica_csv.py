from practica import Automovil, Particular, Carga, Motocicleta, Bicicleta
import csv

def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "w")
    datos = [(Automovil.__class__, Automovil.__dict__)]
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)
    archivo.close()
def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    
    archivo.close()
    return vehiculos

particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

particular =guardar("vehiculos.csv", particular)
carga = guardar("vehiculos.csv", carga)
bicicleta = guardar("vehiculos.csv",bicicleta)
motocicleta = guardar("vehiculos.csv", motocicleta)

