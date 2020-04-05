from tkinter import Tk, filedialog
import AFD2
import graph
import gramatica2 as gram
import os
nombre=""
def ADFarch():
    global nombre
    ls =Tk()
    ls.title("Archivo AFD")
    ls.filename = filedialog.askopenfilename(initialdir="c:/Desktop",title="seleccionar Archivo",filetypes=(("afd files","*.afd"),("all files","*.*")))
    ls.mainloop()
    archivo1 = open(ls.filename,"r")
    text= os.path.splitext(ls.filename)
    text1= text[0].split("/")
    for i in range(len(text1)):
        x=len(text1)
        if x-1==i:
           nombre=text1[i] 
    t=0       
    for obten in archivo1.readlines():
           
        if t==0:
            AFD2.pedirnombre(nombre)
            estado=obten.split(";")
            estado1=estado[0].split(",")
            print(estado1)
            AFD2.estados(estado1[0])
            AFD2.estados(estado1[1])
            AFD2.alfabetos(estado1[2])
            AFD2.inicialstate(estado1[0])
            salto=estado[1] .split("\n")
            bandera=salto[0].split(",")
            if bandera[0]=='true':
                AFD2.finalstate(estado1[0])
            elif bandera[1]=='true':
                AFD2.finalstate(estado1[1])
            AFD2.modo1(''+estado1[0]+','+estado1[1]+';'+estado1[2])    
           
        else:
            #AFD2.pedirnombre(nombre)
            estado=obten.split(";")
            estado1=estado[0].split(",")
            print(estado1)
            AFD2.estados(estado1[0])
            AFD2.estados(estado1[1])
            AFD2.alfabetos(estado1[2])
            #AFD2.inicialstate(estado1[0])
            salto=estado[1] .split("\n")
            bandera=salto[0].split(",")
            if bandera[0]=='true':
                AFD2.finalstate(estado1[0])
            elif bandera[1]=='true':
                AFD2.finalstate(estado1[1])
            AFD2.modo1(''+estado1[0]+','+estado1[1]+';'+estado1[2])
        t+=1        
    text=AFD2.dfagraph+AFD2.auxiliar1+AFD2.auxdfagraph+"}"
    graph.grafic(text,nombre)  
def arcgram():
    global nombre
    ls =Tk()
    ls.title("Archivo Gramatica")
    ls.filename = filedialog.askopenfilename(initialdir="c:/Desktop",title="seleccionar Archivo",filetypes=(("grm files","*.grm"),("all files","*.*")))
    ls.mainloop()
    archivo1 = open(ls.filename,"r")
    text= os.path.splitext(ls.filename)
    text1= text[0].split("/")
    for i in range(len(text1)):
        x=len(text1)
        if x-1==i:
           nombre=text1[i] 
    z=0      
    for obten in archivo1.readlines():  
        letra=obten.split(">")   #una letra del estado de la gramtica 
        letras=obten.split("\n") 
        #nueva=letra[1].replace("", ",")
        letra1=letra[1].split("\n")
        letra2=letra1[0].split(" ")#1,2
        prin=letra[0].split(" ")#0
        tamaño= int(len(letra2))
        if tamaño==3:
            if letra2[2].isupper() or letra2[2]=='epsilon' :
                if z==0:
                    gram.pedirnombre(nombre)
                    gram.estados(prin[0])
                    gram.estados(letra2[2])
                    gram.alfabetos(letra2[1])
                    gram.inicialstate(prin[0])
                    gram.producciones(''+prin[0]+' > '+letra2[1]+''+letra2[2],letras[0])
                else:
                    #gram.pedirnombre(nombre)
                    gram.estados(prin[0])
                    gram.estados(letra2[2])
                    gram.alfabetos(letra2[1])
                    #gram.inicialstate(prin[0])
                    gram.producciones(''+prin[0]+' > '+letra2[1]+''+letra2[2],letras[0])
                    print(prin)   
            elif letra2[1].isupper() or letra2[1]=='epsilon':
                if z==0:
                    gram.pedirnombre(nombre)
                    gram.estados(prin[0])
                    gram.estados(letra2[1])
                    gram.alfabetos(letra2[2])
                    gram.inicialstate(prin[0])
                    gram.producciones(''+prin[0]+' > '+letra2[2]+''+letra2[1],letras[0])
                else:
                    #gram.pedirnombre(nombre)
                    gram.estados(prin[0])
                    gram.estados(letra2[1])
                    gram.alfabetos(letra2[2])
                    #gram.inicialstate(prin[0])
                    gram.producciones(''+prin[0]+' > '+letra2[2]+''+letra2[1],letras[0])
        else:
                 #gram.pedirnombre(nombre)
                gram.estados(prin[0])
                #gram.estados(letra2[1])
                #gram.alfabetos(letra2[2])
                #gram.inicialstate(prin[0])
                gram.producciones(''+prin[0]+' > epsilon',letras[0])                   
        print(letra2[1]) 
        z+=1  
def menuarchivo():
    import menu   
    op = 0
    while op != 4:
        print("=========================================================")
        print("=\t\t 1.   Archivo AFD\t\t\t=") 
        print("=\t\t 2.   Archivo Gramatica\t\t\t=") 
        print("=\t\t 3.   Menu Principal\t\t\t=") 
        print("=========================================================")
        op = str(input("Elige una opcion:\n"))       

        if op == '1' :
            ADFarch()
            break
        elif op == '2' :
            arcgram()
            break 
        elif op == '3':  
            menu.prueba()
        else:
            menuarchivo()                  