from practica import Vehiculo, Automovil

def ingresar_datos():

    for indice in range(num_vehiculos):

        print(f"Datos del automovil:", indice+1)

        auto = Automovil.ingresar_automovil()
        datos_vehiculos.append(auto)

print("PRACTICA DE CONSOLIDACIÓN MODULO 4")
print("**********************************")

datos_vehiculos=[]

num_vehiculos=int(input(f"Cuantos vehículos desea ingresar: "))
ingresar_datos()
print(datos_vehiculos)