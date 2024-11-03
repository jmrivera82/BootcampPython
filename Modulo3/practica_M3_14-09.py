#funciones

def hacer_grandioso(magos):


    for i,j in enumerate(magos):
        
        mago=magos[i]
    
        magos[i]="El gran "+ mago
    
    return magos


def imprimir(magos, cientificos, otros):

    print("Listado de nombres de magos ingresados:")

    for i,j in enumerate(magos):
        
        print(i+1,"-",magos[i])

    print("Listado de nombres de cientificos ingresados:")

    for i,j in enumerate(cientificos):
        
        print(i+1,"-",cientificos[i])

    print("Listado de nombres de otras personas ingresadas:")

    for i,j in enumerate(otros):
        
        print(i+1,"-",otros[i])


def imprimir_nombres(nombres):

    x = len(nombres)
    print("Lista completa de nombres ingresados:")
    for i in range(0,x):
        print (i+1, "-", nombres[i])

#PROGRAMA

nombres=["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]

i = len(nombres)

#defino listas para separar por tipo

magos = []
cientificos = []
otros = []

#asigno los nombres a las listas según el enunciado

for i in nombres:
    
    if i ==  "Harry Houdini" or i== "David Blaine" or i== "Teller":
        magos.append(i)
    
    elif i ==  "Newton" or i == "Hawking" or i == "Einstein":
        cientificos.append(i)

    else:
        otros.append(i)


print("PRACTICA DE CONSOLIDACIÓN MODULO 3")
imprimir_nombres(nombres)
hacer_grandioso(magos)
imprimir(magos,cientificos,otros)

