from practica import Vehiculo, Automovil

print("PRACTICA DE CONSOLIDACIÓN MODULO 4")
print("**********************************")

datos_vehiculos=[]

def ingresar_datos():

    for indice in range(num_vehiculos):

        print(f"Datos del automovil:", indice+1)

        #Se solicitan los datos al usuario mediante inputs

        def ingresarAutomovil(self):
            self.marca=input(f"Ingrese Marca: ")
            self.modelo=input(f"Ingrese Modelo: ")
            self.numeroDeRuedas=input(f"Ingrese Numero de ruedas: ")
            self.velocidad=input(f"Ingrese velocidad: ")
            self.cilindrada=input(f"Ingrese cilindrada: ")
            datos_vehiculos=(self.marca,self.modelo,self.numeroDeRuedas,self.velocidad,self.cilindrada)


num_vehiculos=int(input(f"Cuantos vehículos desea ingresar: "))
ingresar_datos()
print(datos_vehiculos)