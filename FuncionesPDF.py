from reportlab.pdfgen import canvas
from FuncionesQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
fecha_actual = datetime.datetime.now()
ruta = "C:/Users/yesen/OneDrive/Escritorio/funciones/"
nombreArchivo = ruta + "reporteGlobal.pdf_"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+ ".pdf"
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