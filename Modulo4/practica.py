
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
        numeroDeRuedas=input(f"Ingrese Numero de ruedas: ")
        velocidad=input(f"Ingrese velocidad: ")
        cilindrada=input(f"Ingrese cilindrada: ")
        return marca,modelo,numeroDeRuedas,velocidad,cilindrada

    def imprimir_automovil(self):
        return f"Datos del automovil: Marca: {self.marca}, Modelo: {self.modelo}"

