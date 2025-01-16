#Parte 1: diseño de las clases Vehículo y Automóvil

class Vehiculo:

    def __init__(self, marca, modelo, numero_de_ruedas):
        self.marca=marca
        self.modelo=modelo
        self.numero_de_ruedas=numero_de_ruedas

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nNumero de ruedas: {self.numero_de_ruedas}"

    def imprimir_vehiculo(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nNumero de ruedas: {self.numero_de_ruedas}")

class Automovil(Vehiculo):

    def __init__(self, marca, modelo, numero_de_ruedas,velocidad,cilindrada):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nNumero de ruedas: {self.numero_de_ruedas}\nVelocidad: {self.velocidad}\nCilindrada: {self.cilindrada}"


    def agregar_automovil():

        automoviles = {}
        #SE SOLICITA DATO AL USUARIO, VALIDAR QUE SEA NÚMERO Y MAYOR A 0
        while True:
            try:
                cantidad=int(input("Cuantos Vehiculos desea ingresar: "))  

                if(cantidad>0):

                    for indice in range (cantidad):
                        id=indice+1
                        print(f"Datos del automovil:",(id))
                        marca=input("Ingresar marca: ")
                        modelo=input("Ingresar Modelo: ")
                        numero_de_ruedas=input("Ingresar Numero de ruedas: ")
                        velocidad=input("Ingresar Velocidad: ")
                        cilindrada=input("Ingresar Cilindrada: ")

                        auto=Automovil(marca,modelo,numero_de_ruedas,velocidad,cilindrada)

                        automoviles[id]=auto
                        print("**************************************")
                        print("Imprimiendo por pantalla los vehículos\n")
                        for clave,valor in automoviles.items():
                            print(f"Datos del automóvil:{clave}\n{valor}\n")
                        print("**************************************")

                    return automoviles

                else:
                    print("La cantidad ingresada no es válida")

            except ValueError:
                print("Debe ingresar un número")     

class Automovil_tipo_particular(Automovil,Vehiculo):
    
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada,numero_de_puesto):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.numero_de_puesto=numero_de_puesto

    def __str__(self):
        return super().__str__()+f"\nNumero de puesto: {self.numero_de_puesto}"
    
class Automovil_tipo_carga(Automovil,Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
        return super().__str__()+f"\nCarga: {self.carga}"

class Bicicleta(Vehiculo):
    
    def __init__(self, marca, modelo, numero_de_ruedas,tipo_bicicleta ):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo_bicicleta=tipo_bicicleta
    
    def __str__(self):
        return super().__str__()+f"\nTipo: {self.tipo_bicicleta}"
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, numero_de_ruedas, tipo_bicicleta)

