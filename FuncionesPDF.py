from reportlab.pdfgen import canvas
from FuncionesQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
fecha_actual = datetime.datetime.now()
ruta = "C:/Users/yesen/OneDrive/Escritorio/funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf_"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+ ".pdf"
nombreQR = ruta + "miQR.pdf"


def generarPDF(listaNombres, listaEdades, nombre, direccion, NombreCliente, Edad,elegido,Dirección,Empleados, empleado, despensa,
                costo, lista, cantidades, compras, preciouni, contadorElementos,TotalPagar, UsuarioPago, Cambio):
    
    generarQR(nombreQR,"hola desde la funcion")
    c =canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700 
    c.setFont('Helvetica', 20)
    c.drawString(xInicial + 120,yInicial,"dirección")
    c.drawString(xInicial,yInicial,"Nombre")
    c.drawString(320,580, "edad")
    c.setFont('Helvetica', 15)
    c.drawString(220,750,"BIENVENIDOS MATERIAS PRIMAS")
    c.setFont('Helvetica', 12)
    c.setFont('Helvetica', 12)
    c.drawString(120,730,f"cliente:  {nombre}")
    c.drawString(120,700,f"Dirección: {direccion}")
    c.drawString(320,580, "$")
    c.drawString(320,560, "$")
    c.drawString(320,540, "$")
    c.drawString(320,520, "$")
    c.drawString(320,500, "$")
    c.drawString(390,580, "$")
    c.drawString(390,560, "$")
    c.drawString(390,540, "$")
    c.drawString(390,520, "$")
    c.drawString(390,500, "$")
    for a,a2,a3,a4 in zip(despensa,cantidades,preciouni,compras):
        c.drawString(120,623, "______________________________________________")
        c.drawString(120,610, "Nombre Producto")
        c.drawString(230,610, "Cantidad")
        c.drawString(310,610, "Precio/pieza")
        c.drawString(400,610, "Total")
        c.drawString(120,608, "______________________________________________")
        #c.drawString(PosX,PosY,f"{a}                       {a2}                       {a3}               {a4}")
        #PosX = PosX-10
        #PosY = PosY-20
    c.drawString(280,470,"Total de pagar: "+str(TotalPagar))
    c.drawString(280,450,"Recibo: "+str(UsuarioPago))
    if(UsuarioPago<TotalPagar):
         c.drawString(280,450,"Lo siento, pero te falta dinero para pagar el total")
    else:
        c.drawString(280,430,"Cambio: "+str("{:.2f}".format(Cambio)))
    
        c.drawString(280,410,"Total de productos vendidos:  "+str(contadorElementos))
    #c.drawString(120,670,f"Correo electrónico: {}")
    
    c.drawImage(nombreQR,200,400,100,100)
    
    for i in range(len(listaNombres)):
        c.setFont('Helvetica', 18)
        yInicial = yInicial - 20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial + 120,yInicial,listaNombres[i])
      
    c. save()
    print("reporte generado--------")