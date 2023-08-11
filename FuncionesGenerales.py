from FuncionesPDF import *
from DatosEstaticos import *
NombreCliente = []
listaNombres = []
listaEdades= []
Edad = []
elegido = []
Dirección = []
Empleados = ["Juan ", "Pedro ", "Pablo ", "vitor ", "Albertano "]
empleado = []
despensa = ["1. Azucar", "2. Harina", "3. Manteca/Puerco", "4. Manteca/Vegetal", "5. Termico #32 L", "6. Termico #32 1/2", "7.Termico #16",
            "8. Termico #12", "9. Termico #10", "10. Termico #4j4", "11. Termico #6j6", "12. Arroz Saman", "13. Arroz Morelos","14. Frijol",
            "15. Alpiste/Simple", "16. Alpiste/Compuesto", "17. Charrola 07", "18. Charrola 855", "19. Charrola 066", "20. Aceite L1/2",
            "21. Aceite L", "22. Aceite 1/2", "23. Canoil", "24. Soya Plus", "25. Nutrioli", "26. Aceite 5L", "27. Levadora","28. Galletas/Mexicanas",
            "29. Maiz/Quebrado", "30. Mantequilla"]
costo = [30,20,35,20,14,12,65,32,6,21,545,55,55,55,7,8,98,75,45,55,55,65,55,12,12,35,65,65,54,60]
lista = ["1.-","2.-","3.-","4.-","5.-", "6.-","7.-","8.-","9.-","10.-", "11.-","12.-","13.-","14.-","15.-",
         "16.-","17.-","18.-","19.-","20.-","21.-","22.-","23.-","24.-","25.-", "26.-","27.-","28.-","29.-","30.-"]
cantidades = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
compras = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
preciouni = [30,20,35,20,14,12,65,32,6,21,545,55,55,55,7,8,98,75,45,55,55,65,55,12,12,35,65,65,54,60]
opcion=1
contadorElementos = 0
nombre = []
direccion = []
TotalPagar = []
UsuarioPago = []
Cambio = []

def menu():
    opcion = 1

    while(opcion!=0):
        print("BIENVENIDOS MATERIAS PRIMAS")
        print("1. Nombre empleado/Num")
        print("2. Nombre cliente/Dirrección")
        print("3. Solicitudes")
        print("4. Listas productos")
        print("5. Generar PDF")
        print("6. Generar QR")
        print("7. Imprimir datos")
        print("0. Salir")
        opcion = int(input("Elige una opcion "))
        if(opcion==1):
            RegistroEmpleado()
        elif(opcion==2):
            RegistroCliente()
        elif(opcion==3):
            solicitud()
        elif(opcion==4):
            ProductosElegido()
#       elif(opcion==5):
#          listarProductos()
        elif(opcion==5):
            generarPDF(listaNombres, listaEdades, nombre, direccion, NombreCliente, Edad,elegido,Dirección,Empleados, empleado, despensa,
                       costo, lista, cantidades, compras, preciouni, contadorElementos,TotalPagar, UsuarioPago, Cambio )
        elif(opcion==7):
            ImprimirDatos()



def RegistroEmpleado():
    elegido = int(input("Numero de Empleado : "))
    elegido = elegido -1

    if elegido > 0 or elegido < len(Empleados):
        print("Atendido por:", Empleados[elegido])
    else:
        print("No existe el Número de Empleado")
        
def RegistroCliente():
    NombreCliente.append(input("Nombre Cliente "))
    Edad.append(input("Edad "))
    Dirección.append(input("Dirrección "))
    Dirección == "1. palmitas, 2. ocampo, 3. guerrero"    
    print("informacion del cliente ")
    print("nombre ",NombreCliente)
    print("edad ",Edad)
    print("direccion",Dirección) 
    
    print("Guardado")
    
    
def solicitud():
    
    solicitud = input("Ingrese el tipo de solicitud (WhatsApp, Telefónica, Personal): ")
    if solicitud.lower() == "whatsapp":
       print("Solicitud WhatsApp.")
    elif solicitud.lower() == "telefonica":
       print("Solicitud telefónica.")
    elif solicitud.lower() == "personal":
       print("Solicitud personal.")
    else:
       print("Tipo de solicitud inválido")

def ProductosElegido():
 print("   |Costo|     |Nombre del producto|")
for i,i2,i3 in zip (despensa, costo, lista):
       print(i3,"$",i2,"       ",i)
       
while opcion == 1:
    opcion2 = int(input("Selecciona alguno de los siguientes productos: "))
    if (opcion2==1):
        piezas = int(input("¿Azucar? "))
        cantidades[0] = cantidades[0]+piezas
        compras[0] = (cantidades[0]*costo[0])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1.Si 2.No "))
    elif(opcion2==2):
        piezas = int(input("¿Harina? "))
        cantidades[1] = cantidades[1]+piezas
        compras[1] = (cantidades[1]*costo[1])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==3):
        piezas = int(input("¿Manteca/Puerco? "))
        cantidades[2] = cantidades[2]+piezas
        compras[2] = (cantidades[2]*costo[2])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==4):
        piezas = int(input("¿Manteca/Vegetal? "))
        cantidades[3] = cantidades[3]+piezas
        compras[3] = (cantidades[3]*costo[3])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==5):
        piezas = int(input("¿Termico #32 L? "))
        cantidades[4] = cantidades[4]+piezas
        compras[4] = (cantidades[4]*costo[4])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==6):
        piezas = int(input("¿Termico #32 1/2? "))
        cantidades[5] = cantidades[5]+piezas
        compras[5] = (cantidades[5]*costo[5])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==7):
        piezas = int(input("¿Termico #16? "))
        cantidades[6] = cantidades[6]+piezas
        compras[6] = (cantidades[6]*costo[6])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==8):
        piezas = int(input("¿Termico #12? "))
        cantidades[7] = cantidades[7]+piezas
        compras[7] = (cantidades[7]*costo[7])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==9):
        piezas = int(input("¿Termico #10? "))
        cantidades[8] = cantidades[8]+piezas
        compras[8] = (cantidades[8]*costo[8])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==10):
        piezas = int(input("¿Termico #4j4? "))
        cantidades[9] = cantidades[9]+piezas
        compras[9] = (cantidades[9]*costo[9])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==11):
        piezas = int(input("¿11. Termico #6j6? "))
        cantidades[10] = cantidades[10]+piezas
        compras[10] = (cantidades[10]*costo[10])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==12):
        piezas = int(input("¿Arroz Saman? "))
        cantidades[11] = cantidades[11]+piezas
        compras[11] = (cantidades[11]*costo[11])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==13):
        piezas = int(input("¿Arroz Morelos? "))
        cantidades[12] = cantidades[12]+piezas
        compras[12] = (cantidades[12]*costo[12])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==14):
        piezas = int(input("¿Frijol? "))
        cantidades[13] = cantidades[13]+piezas
        compras[13] = (cantidades[13]*costo[13])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==15):
        piezas = int(input("¿Alpiste/Simple? "))
        cantidades[14] = cantidades[14]+piezas
        compras[14] = (cantidades[14]*costo[14])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==16):
        piezas = int(input("¿Alpiste/Compuesto? "))
        cantidades[15] = cantidades[15]+piezas
        compras[15] = (cantidades[15]*costo[15])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==17):
        piezas = int(input("¿Charrola 07? "))
        cantidades[16] = cantidades[16]+piezas
        compras[16] = (cantidades[16]*costo[16])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==18):
        piezas = int(input("Charrola 855¿? "))
        cantidades[17] = cantidades[17]+piezas
        compras[17] = (cantidades[17]*costo[17])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==19):
        piezas = int(input("¿Charrola 066? "))
        cantidades[18] = cantidades[18]+piezas
        compras[18] = (cantidades[18]*costo[18])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==20):
        piezas = int(input("¿Aceite L1/2? "))
        cantidades[19] = cantidades[19]+piezas
        compras[19] = (cantidades[19]*costo[19])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==21):
        piezas = int(input("¿Aceite L? "))
        cantidades[20] = cantidades[20]+piezas
        compras[20] = (cantidades[20]*costo[20])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==22):
        piezas = int(input("¿Aceite 1/2? "))
        cantidades[21] = cantidades[21]+piezas
        compras[21] = (cantidades[21]*costo[21])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==23):
        piezas = int(input("¿Canoil? "))
        cantidades[22] = cantidades[22]+piezas
        compras[22] = (cantidades[22]*costo[22])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==24):
        piezas = int(input("¿Soya Plus? "))
        cantidades[23] = cantidades[23]+piezas
        compras[23] = (cantidades[23]*costo[23])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==25):
        piezas = int(input("¿Nutrioli? "))
        cantidades[24] = cantidades[24]+piezas
        compras[24] = (cantidades[24]*costo[24])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==26):
        piezas = int(input("¿Aceite 5L? "))
        cantidades[25] = cantidades[25]+piezas
        compras[25] = (cantidades[25]*costo[25])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==27):
        piezas = int(input("¿Levadora? "))
        cantidades[26] = cantidades[26]+piezas
        compras[26] = (cantidades[26]*costo[26])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==28):
        piezas = int(input("¿Galletas/Mexicanas? "))
        cantidades[27] = cantidades[27]+piezas
        compras[27] = (cantidades[27]*costo[27])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==29):
        piezas = int(input("¿Maiz/Quebrado? "))
        cantidades[28] = cantidades[28]+piezas
        compras[28] = (cantidades[28]*costo[28])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    elif(opcion2==30):
        piezas = int(input("¿Mantequilla?"))
        cantidades[29] = cantidades[29]+piezas
        compras[29] = (cantidades[29]*costo[29])
        contadorElementos=contadorElementos+piezas
        opcion = int(input("¿Quieres comprar algo mas? 1-Si 2.No "))
    else:
        print("Producto que no esta en el menu, no esta disponible ")

print("compras: ")
print(" ")
print("|Nombre del producto|   |Cantidad|   |Precio del producto|   |TotalProducto|")

for i,i2,i3,i4 in zip(cantidades, costo, compras, despensa):
    print(" ",i,"           ","$",i2,"                  ","$",i3,"               ","",i4,"")

TotalPagar = sum(compras)

print("El total de pagar es: $",TotalPagar)
Pago = input("Recibo $")
UsuarioPago = float(Pago)
Cambio = UsuarioPago-TotalPagar
print("El usuario pago un total de: $",UsuarioPago)
if (UsuarioPago<TotalPagar):
   print("no puedes llevar los productos")
else:
    print("Tu cambio es: $"+"{:.2f}".format(Cambio))

print("Articulos vendidos: ",contadorElementos)

def ImprimirDatos():
    for i in range(len(NombreCliente)):
        print(f"Nombre: {NombreCliente[i]}  Edda:{Edad[i]}  Dirección:{Dirección[i]} ")
        
