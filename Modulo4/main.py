from practica import Vehiculo, Automovil

def ingresar_datos():

    for indice in range(num_vehiculos):

        print(f"Datos del automovil:", indice+1)

        autos = Automovil.ingresar_automovil()
        datos_vehiculos.append(autos)

print("PRACTICA DE CONSOLIDACIÓN MODULO 4")
print("**********************************")

datos_vehiculos=[]

num_vehiculos=int(input(f"Cuantos vehículos desea ingresar: "))
ingresar_datos()
#print(datos_vehiculos) -- prueba de impresión de los vehiculos ingresados

print(f"Imprimiendo por pantalla los vehículos: ")
#error AttributeError: 'tuple' object has no attribute 'imprimir_automovil'
for autito in datos_vehiculos:
    autito.imprimir_automovil(self)


