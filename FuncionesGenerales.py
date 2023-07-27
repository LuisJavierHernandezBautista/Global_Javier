from FuncionesPDF import *
from DatosEstaticos import *
listaNombres = []
listaEdades = []
#cantidades = []
#compras = [] 
#costo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
def menu():
    opcion = 1
    
    while(opcion!=0):
        print("1. Pedir datos")
        print("2. Imprimir datos")
        print("3. Generar PDF")
        print("4. Generar QR")
        print("5. Listas productos")
        print("0. Salir")
        opcion = int(input("Elige una opcion "))
        if(opcion==1):
            pedirDatos()
        elif(opcion==2):
            ImprimirDatos()
        elif(opcion==3):
            generarPDF(listaNombres,listaEdades)
        elif(opcion==5):
            listarProductos()

def pedirDatos():
    listaNombres.append(input("Ingresa un nombre "))
    listaEdades.append(input("Ingresa una edad "))
    print("Guardado")

def ImprimirDatos():
    for i in range(len(listaNombres)):
        print(f"Nombre: ) {listaNombres[i]} Edad: {listaEdades[i]}")

#def listarProducto():    
    
    #piezas = int(input("¿Cuantas paquetes de levadoras quieres? "))
    #cantidades[0] = cantidades[0]+piezas
    #compras[0] = (cantidades[0]*costo[0])
    #contadorElementos=contadorElementos+piezas