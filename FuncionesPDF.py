from reportlab.pdfgen import canvas
from FuncionesQR import *
ruta = "C:/Users/yesen/OneDrive/Escritorio/funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"
nombreQR = ruta + "miQR.pdf"

def generarPDF(listaNombres, listaEdades):
    generarQR(nombreQR,"hola desde la funcion")
    c =canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700 
    c.setFont('Helvetica', 20)
    c.drawString(xInicial,yInicial,"edad")
    c.drawString(xInicial + 120,yInicial,"Nombre")
    
    c.drawImage(nombreQR,200,400,100,100)
    
    for i in range(len(listaNombres)):
        c.setFont('Helvetica', 18)
        yInicial = yInicial - 20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial + 120,yInicial,listaNombres[i])
      
    c. save()
    print("reporte generado--------")