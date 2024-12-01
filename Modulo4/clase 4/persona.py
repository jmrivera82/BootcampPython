class Persona:
    def __init__(self, nombre, apellido, cedula):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula


    def imprimirPersona(self):
        print(f"Nombre: {self.nombre} \nApellido: {self.apellido} \nCedula: {self.cedula}")


    def __str__(self):
        return f"Nombre: {self.nombre} \nApellido: {self.apellido} \nCedula: {self.cedula}"
   
    #herencia

class Supervisor(Persona):
    def __init__(self, nombre, apellido, cedula, zona):
        super().__init__(nombre,apellido, cedula)
        self.zona=zona

    def imprimirSupervisor(self):
        super().imprimirPersona() 
        print("Zona: ",self.zona)

    def __str__ (self):
        return f"{super().__str__()} \nZona: {self.zona}"  

class Cliente(Persona):
    def __init__(self, nombre, apellido, cedula, descuento):
        super().__init__(nombre, apellido,cedula)
        self.descuento=descuento

    def imprimircliente(self):
        super().imprimirPersona()
        print("Descuento:", self.descuento)

    def __str__(self):
        #return super().__str__() , f"descuento: {self.descuento}"
        pass