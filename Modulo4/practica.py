
class Vehiculo:

    def __init__(self, marca, modelo, numeroDeRuedas):
        self.marca=marca
        self.modelo=modelo
        self.numeroDeRuedas=numeroDeRuedas

class Automovil:

    def __init__(self):
        self.marca=""
        self.modelo=""
        self.numeroDeRuedas=numeroDeRuedas
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def ingresar_automovil():
        marca=input(f"Ingrese Marca: ")
        modelo=input(f"Ingrese Modelo: ")
        numero_de_ruedas=input(f"Ingrese Numero de ruedas: ")
        velocidad=input(f"Ingrese velocidad en km/h: ")
        cilindrada=input(f"Ingrese cilindrada en cc : ")
        return marca,modelo,numero_de_ruedas,velocidad,cilindrada

    def imprimir_automovil(self):
        print(f"Datos del automovil: Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} Ruedas, {self.velocidad} Km/h, {self.cilindrada} cc")

