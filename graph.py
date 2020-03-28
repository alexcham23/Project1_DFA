import io
import os
import sys
#from reportlab.pdfgen import canvas
#from reportlab.platypus import Spacer
#from reportlab.platypus import Imagen
from graphviz import Digraph
from graphviz import Source
import os.path as path
from PIL import Image
lista=[]
dot=""
ruta=""
#grafo='digraph "finite_state_machine" {rankdir=LR;size="42,42"  EMPTY [style=invis]  EMPTY [shape=point] node [shape = doublecircle]; Q6; Q4; node [shape = circle]; EMPTY ->Q0 [ label = "" ]; Q0 -> Q2 [ label = "b" ]; Q0 -> Q3 [ label = "a" ]; Q0 -> Q1 [ label = "?" ]; Q1 -> Q0 [ label = "?" ]; Q1 -> Q4 [ label = "?" ]; Q2 -> Q1 [ label = "?" ]; Q3 -> Q1 [ label = "?" ]; Q4 -> Q4 [ label = "a" ]; Q4 -> Q5 [ label= "?" ]; Q5 -> Q7 [ label = "b" ];Q5 -> Q8 [ label = "a" ];Q7 -> Q6 [ label = "?" ];Q8 -> Q6 [ label = "?" ];}'
def graficador():
     global ruta
     ruta = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')+"\\ruta"
     print(ruta)
    # try:
     if os.path.isdir(ruta):
        #prueba()     
        print("la carpeta ya existe en el Dirrectorio")
       # grafic(grafo)
     else:    
        os.mkdir(ruta)
        print()
     #except OSError:
            #print("La creación del directorio %s falló" % ruta)
    # else:
     #prueba()       #  print("Se ha creado el directorio: %s " % ruta)
def grafic(grafo, name): 
   global ruta,lista
   if path.exists(''+ruta+'\\'+name+'.dot'):
      os.remove(''+ruta+'\\'+name+'.dot') 
      os.remove(''+ruta+'\\'+name+'.dot.png')    
      #d = Digraph(format='png')
      d=Source(str(grafo))
      #d.source(grafo)
      d.format='png'
      d.render(''+name+'.dot', ruta,view=True) 
   else:
      #d = Digraph(format='png')
      d=Source(str(grafo))
      #d.source(grafo)
      d.format='png'
      #d.format='pdf'
      d.render(''+name+'.dot',ruta,view=True)
      im=Image.open(ruta+'\\'+name+'.dot.png')
      imagen=im.convert('RGB')
      lista.append(imagen)
      #Pdf()
     
def Pdf():
   global ruta,lista
   x=0
   im=''
   aux=[]
   while x<int(len(lista)):
         if x==0:
             im=lista[x]
         else:
               aux.append(lista[x])   
         x+=1       
   pdfname=ruta+'\\nose.pdf' 
   if path.exists(pdfname): 
      os.remove(pdfname)     
      im.save(pdfname,"PDF",resolution=100, save_all=True, append_images=aux)       
   else:
      im.save(pdfname,"PDF",resolution=100,save_all=True, append_images=aux)
'''
   lista.append(ruta+'\\master.dit.png')
   image=Image.save(ruta+'\\apn.png')
           
       c= canvas.Canvas(ruta+'\\resumengrafic.pdf')
       c.drawImage(archivo,10,10,10,10)
       c.showPage()
       c.save()
'''
'''       
def prueba():
    global lista
    image1 = Image.open(r''+ruta+''+'\\descarga.png')
    #lista.append(image1)
    image2 = Image.open(r''+ruta+'\\descarga1.png')
    #lista.append(image2)
    image3 = Image.open(r''+ruta+'\\descarga2.png')
    #lista.append(image1)
    image4 = Image.open(r''+ruta+'\\descarga3.png')
    size=25,25
    
    im1 = image1.convert('RGB')
    im1.thumbnail(size)
    lista.append(im1)
    im2 = image2.convert('RGB')
    im2.resize((120,240))
    lista.append(im2)
    im3 = image3.convert('RGB')
    im3.thumbnail(size)
    lista.append(im3)
    im4 = image4.convert('RGB')
    im4.thumbnail(size)
    lista.append(im4)   
    
    Pdf()
'''    
graficador()
