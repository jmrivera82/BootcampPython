nombres=["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]

magos=["Harry Houdini","David Blaine","Teller"]
cientificos=["Newton","Hawking","Einstein"]
otros=["Messi","Pele","Juanes"]


def hacer_grandioso(magos):

    x = len(magos)
    print("Listado de magos grandiosos:")

    for i in range (0,x):

        magos[i]="El gran "+ magos[i]
        print(i+1, "-", magos[i])

def imprimir_nombres(nombres):

    x = len(nombres)
    print("Lista completa de nombres ingresados:")
    for i in range(0,x):
        print (i+1, "-", nombres[i])

def imprimir_cientificos(cientificos):
    x = len(cientificos)
    print("Listado de nombres de científicos ingresados:")
    for i in range(0,x):
        print (i+1, "-", cientificos[i])
        
def imprimir_resto(otros):
    x = len(otros)
    print("Listado de otros nombres ingresados:")
    for i in range(0,x):
        print (i+1, "-", otros[i])
    
imprimir_nombres(nombres)
hacer_grandioso(magos)
imprimir_cientificos(cientificos)
imprimir_resto(otros)
