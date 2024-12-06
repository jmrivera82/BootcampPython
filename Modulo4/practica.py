
class Vehiculo:

    def __init__(self, marca, modelo, numero_de_ruedas):
        self.marca=marca
        self.modelo=modelo
        self.numero_de_ruedas=numero_de_ruedas

class Automovil:

    def __init__(self,marca,modelo,numero_de_ruedas,velocidad,cilindrada):
        self.marca=marca
        self.modelo=modelo
        self.numero_de_ruedas=numero_de_ruedas
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


#prueba instanciando la clase Automovil

#automovil1=Automovil("aa","bb",4,180,50)
#automovil2=Automovil("cc","aa",4,200,50)
#automovil3=Automovil("tt","rr",4,220,50)

#automovil1.imprimir_automovil()
#automovil2.imprimir_automovil()
#automovil3.imprimir_automovil()