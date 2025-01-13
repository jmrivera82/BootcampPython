from practica import Vehiculo, Automovil

def ingresar_datos():

    datos_vehiculos=[]

    for indice in range(num_vehiculos):
       print(f"Datos del automovil:", indice+1)

       autos = Automovil.ingresar_automovil()
       datos_vehiculos.append(autos)

       print(f"Imprimiendo por pantalla los vehículos: ")

       for autito in datos_vehiculos:
            #autito.imprimir_automovil()
            print(datos_vehiculos)


#Programa

print("PRACTICA DE CONSOLIDACIÓN MODULO 4")
print("**********************************")
num_vehiculos=int(input(f"Cuantos vehículos desea ingresar: "))
ingresar_datos()
#print(datos_vehiculos) -- prueba de impresión de los vehiculos ingresados




