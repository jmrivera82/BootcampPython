from practica import Vehiculo, Automovil, Carga, Particular, Bicicleta, Motocicleta

#PROGRAMA

print("*****PRACTICA DE CONSOLIDACIÓN MODULO 4*****")

print("Parte 1")
print("Generar instancias de automóvil")
print("*"*40)
Automovil.agregar_automovil()
print("Parte 2")
print("Generar instancias de Particular, Carga, Bicicleta y Motocicleta")
print("*"*40)
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
print(f"Marca: {particular.marca}, Modelo: {particular.modelo}, {particular.numero_de_ruedas} ruedas {particular.velocidad} km/h, {particular.cilindrada} cc, Puestos: {particular.numero_de_puesto}")
print(f"Marca: {carga.marca}, Modelo: {carga.modelo}, {carga.numero_de_ruedas} ruedas, {carga.velocidad} km/h, {carga.cilindrada} cc, Carga: {carga.carga}")
print(f"Marca: {bicicleta.marca}, Modelo: {bicicleta.modelo}, {bicicleta.numero_de_ruedas} ruedas, Tipo: {bicicleta.tipo_bicicleta}")
print(f"Marca: {motocicleta.marca}, Modelo: {motocicleta.modelo}, {motocicleta.numero_de_ruedas} ruedas, Tipo: {motocicleta.tipo_bicicleta}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro radios: {motocicleta.nro_radios}")

print("*"*40)
print("Verificación de instancias")
print("*"*40)

print("Motocicleta es instancia con relación a Vehículo:",isinstance(motocicleta,Vehiculo))
print("Motocicleta es instancia con relación a Automóvil:",isinstance(motocicleta,Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:",isinstance(motocicleta,Particular))
print("Motocicleta es instancia con relación a Vehículo de carga:",isinstance(motocicleta,Carga))
print("Motocicleta es instancia con relación a Bicicleta:",isinstance(motocicleta,Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:",isinstance(motocicleta,Motocicleta))