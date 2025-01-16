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
                        print("*"*40)
                        print("Imprimiendo por pantalla los vehículos\n")
                        for clave,valor in automoviles.items():
                            print(f"Datos del automóvil:{clave}\n{valor}\n")
                        print("*"*40)

                    return automoviles

                else:
                    print("La cantidad ingresada no es válida")

            except ValueError:
                print("Debe ingresar un número")     

class Particular(Automovil,Vehiculo):  #El ejercicio indica como se debe llamar la clase al mostrar el código de la instancia
    
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada,numero_de_puesto):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.numero_de_puesto=numero_de_puesto

    def __str__(self):
        return super().__str__()+f"\nNumero de puesto: {self.numero_de_puesto}"
    
class Carga(Automovil,Vehiculo): #El ejercicio indica como se debe llamar la clase al mostrar el código de la instancia
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
        return super().__str__()+f"\nCarga: {self.carga}"

class Bicicleta(Vehiculo): #El ejercicio indica como se debe llamar la clase al mostrar el código de la instancia
    
    def __init__(self, marca, modelo, numero_de_ruedas,tipo_bicicleta ):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo_bicicleta=tipo_bicicleta
    
    def __str__(self):
        return super().__str__()+f"\nTipo: {self.tipo_bicicleta}"
    
class Motocicleta(Bicicleta): #El ejercicio indica como se debe llamar la clase al mostrar el código de la instancia
    def __init__(self, marca, modelo, numero_de_ruedas, tipo_bicicleta,nro_radios,cuadro,motor):
        super().__init__(marca, modelo, numero_de_ruedas, tipo_bicicleta)
        self.nro_radios=nro_radios
        self.cuadro=cuadro
        self.motor=motor

    def __str__(self):
        return super().__str__()+f"\nNro radios: {self.nro_radios} - motor: {self.motor}"

