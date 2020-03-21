import io
import os
import sys
from graphviz import Digraph
from graphviz import Source

dot=""
ruta=""
grafo='digraph "finite_state_machine" {rankdir=LR;size="42,42"  EMPTY [style=invis]  EMPTY [shape=point] node [shape = doublecircle]; Q6; Q4; node [shape = circle]; EMPTY ->Q0 [ label = "" ]; Q0 -> Q2 [ label = "b" ]; Q0 -> Q3 [ label = "a" ]; Q0 -> Q1 [ label = "?" ]; Q1 -> Q0 [ label = "?" ]; Q1 -> Q4 [ label = "?" ]; Q2 -> Q1 [ label = "?" ]; Q3 -> Q1 [ label = "?" ]; Q4 -> Q4 [ label = "a" ]; Q4 -> Q5 [ label= "?" ]; Q5 -> Q7 [ label = "b" ];Q5 -> Q8 [ label = "a" ];Q7 -> Q6 [ label = "?" ];Q8 -> Q6 [ label = "?" ];}'
def graficador():
     global ruta,grafo
     ruta = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')+"\\ruta"
    # try:
     if os.path.isdir(ruta):
        print("la carpeta ya existe en el Dirrectorio")
        grafic(grafo)
     else:    
        os.mkdir(ruta)
        print()
     #except OSError:
            #print("La creación del directorio %s falló" % ruta)
    # else:
          #  print("Se ha creado el directorio: %s " % ruta)
def grafic(grafo):  
      #d = Digraph(format='png')
      d=Source(str(grafo))
      #d.source(grafo)
      d.format='png'
      d.render('anti.dot', ruta,view=True)

graficador()
