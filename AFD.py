import os
import graph
#import ptvsd; print(ptvsd.__version__)
nombre=""
estado=[]
alfabeto=[]
inicial=[]
#final=[]
aceptacion=[]
transiciones=[]
banderamenu= 0
banderaestado=False
banderatransi=False
lista=[]
dfagraph=""
auxdfagraph=""
auxiliar1='node [shape = circle];\n'
def menuAFD():
    global banderamenu,banderaestado
    op = 0
    while op != 8:
        print("=========================================================")
        print("=\t\t 1.   Ingresar Estados\t\t\t=") 
        print("=\t\t 2.   Ingresar Alfabeto\t\t\t=") 
        print("=\t\t 3.   Estado Inicial\t\t\t=") 
        print("=\t\t 4.   Estado de Aceptacion\t\t=")
        print("=\t\t 5.   Transiciones \t\t\t=") 
        print("=\t\t 6.   Ayuda\t\t\t\t=")
        print("=\t\t 7.   Menu Principal\t\t\t=") 
        print("=========================================================")
        op = str(input("Elige una opcion:\n"))       

        if op == '1' :
            banderamenu=1
            estados()
            break
        elif op == '2' :
            if(banderaestado==True):
                banderamenu=2
                alfabetos()
            else:
                os.system("cls")
                print("por favor ingrese de primero los estados\n")
                menuAFD()    
            break
        elif op == '3' :
            if banderaestado==True :
                banderamenu=3
                inicialstate()
            else:
                os.system("cls")
                print("por favor ingrese los estados\n")
                menuAFD()     
            break
        elif op == '4' :
            if banderaestado==True :
                banderamenu=4
                finalstate()
            else:
                os.system("cls")
                print("por favor ingrese los estados\n")
                menuAFD() 
            break
        elif op == '5' :
            if banderaestado==True :
                menumodo()
            else:
                os.system("cls")
                print("por favor ingrese los estados\n")
                menuAFD() 
            break
        elif op == '6' :
            banderamenu=7
            break
        elif op == '7' :
            print("hola")
            break
        else:
            menuAFD()

def pedirnombre():
    global nombre,estado,alfabeto,inicial,aceptacion,transiciones,lista,dfagraph
    nombre= str(input("Ingrese Un nombre para el AFD:\n "))
    if nombre=="" or nombre=="\t":
        os.system("cls")
        pedirnombre()
    else:    
        guardar=nombre,estado,alfabeto,inicial,aceptacion,transiciones
        lista.append(guardar)
        dfagraph="digraph \""+nombre+"\" {\n"
        dfagraph+="rankdir=LR;\nsize=\"42,42\"  EMPTY [style=invis]  EMPTY [shape=point] node [shape = doublecircle];\n"
        menuAFD()
        imprimir()
def imprimir():
    global lista
    for x in lista:
        print(x)
def estados():
    global nombre,lista,banderaestado
   
    estado= str(input("Ingrese un estado:\n"))
    banderaestado=True
    bandera = False
    if estado=="" or estado=="\t":
        os.system("cls")
        estados()
    else:   
        for busca in lista:
            if busca[0] == nombre:
                x=0
                if not busca[1]:#verificamos si lista de estados esta vacia
                    busca[1].append(estado)
                
                elif busca[1]:# de caso contrario no esta vacia    
                    while x < int(len(busca[1])) and bandera ==False:# verificamos el tamaño de la lista estado
                        if busca[1][x] == estado:# verificamos si existe un estado repetido
                            print("este Estado ya existe") 
                            bandera = True
                        x+=1    
                     
                    if bandera== False:#guardamos el estado si no se encuentra repetido
                        busca[1].append(estado)
                   
                        
    menupreg()                
def alfabetos():
    global nombre,lista
    bandera1=False
    bandera2=False
    alfabeto=str(input("Ingrese un alfabeto:\n"))
    if alfabeto=="" or alfabeto=="\t":
        os.system("cls")
        alfabeto()
    else:
        for busca in lista:
            if busca[0]==nombre:
                if not busca[2]:
                    x=0
                    while x < int(len(busca[1])) and bandera1==False :
                        if busca[1][x]==alfabeto:
                            print("EL alfabeto "+alfabeto+" debe de ser diferente al nombre del estado")
                            bandera1=True
                        x+=1
                    if bandera1== False:
                        busca[2].append(alfabeto)
                elif busca[2]:
                    if bool(alfabeto in busca[2])==False:
                        y=0
                        while y<int(len(busca[1])) and bandera2==False: 
                            if busca[1][y]==alfabeto:
                                bandera2=True
                            y+=1
                        if bandera2== False:
                            busca[2].append(alfabeto)
                        elif bandera2==True: 
                            print("EL alfabeto "+alfabeto+" debe de ser diferente al nombre del estado")    
                    elif bool(alfabeto in busca[2])==True:
                        print("El alfabeto "+alfabeto+" ya existe en la Base de datos")  
    menupreg()
def inicialstate():
    global lista,nombre,auxiliar1
    bandera =False
    iniciales = str(input("Ingrese el estado inicial:\n"))
    if iniciales =="" or iniciales=="\t":
        os.system("cls")
        inicialstate()
    else:
        for buscar in lista:
            if buscar[0]==nombre:
                if  not buscar[3]:# verifica si esta vacia regresara un true o false
                    x=0
                    while x <int(len(buscar[1])) and bandera == False: 
                        if buscar[1][x] == iniciales:
                            bandera = True
                        x+=1
                    if bandera == True:
                        buscar[3].append(iniciales)
                    if bandera == False:
                        print(iniciales+" no existe en los estados")    
                elif buscar[3]:
                    
                    y=0
                    while y <int(len(buscar[1])) and bandera == False: 
                        if buscar[1][y] == iniciales:
                            bandera = True
                        y+=1
                    if bandera == True and banderatransi==False:
                        #buscar[3].insert(0,iniciales)
                        buscar[3][0]=str(iniciales)
                    elif bandera == True and banderatransi==True: # aqui tenco que rebobinar para graphiz
                        auxiliar1='node [shape = circle];\n'
                        buscar[3][0]=str(iniciales)
                        auxiliar1+='EMPTY -> '+buscar[3][0]+' [ label = "" ];\n'
                    elif bandera == False:
                        print(iniciales+" no existe en los estados")     
    menupreg()     
def finalstate():
    global lista,nombre,dfagraph
    bandera =False
    iniciales = str(input("Ingrese el estado finales:\n"))
    if iniciales =="" or iniciales=="\t":
        os.system("cls")
        inicialstate()
    else:
        for buscar in lista:
            if buscar[0]==nombre:
                if  not buscar[4]:# verifica si esta vacia regresara un true o false
                    x=0
                    while x <int(len(buscar[1])) and bandera == False: 
                        if buscar[1][x] == iniciales:
                            bandera = True
                        x+=1
                    if bandera == True:
                        buscar[4].append(iniciales)
                        dfagraph+=""+iniciales+";\n"
                    elif bandera == False:
                        print(iniciales+" no existe en los estados")    
                elif buscar[3]:
                    if bool(iniciales in buscar[4])== False:
                        y=0
                        while y <int(len(buscar[1])) and bandera == False: 
                            if buscar[1][y] == iniciales:
                                bandera = True
                            y+=1
                        if bandera == True:
                            #buscar[3].insert(0,iniciales)
                            buscar[4].append(iniciales)
                            dfagraph+=""+iniciales+";\n"
                        elif bandera == False:
                            print(iniciales+" no existe en los estados")  
                    elif bool(iniciales in buscar[4]) ==True:
                        print(iniciales+" Error ya exist dentro de los estdos FInales")

    menupreg()       
def modo1():
    global lista,nombre,banderatransi,auxiliar1,auxdfagraph
    transicion1=str(input("ingrese las transiciones de esta manera sin parentesis (estado1,estado2;alfabeto):\n"))
    if transicion1=="" or transicion1=="\t":
        os.system("cls")
        modo1()
    else:
        for busca in lista:
            sl=transicion1.split(";")
            sl2=sl[0].split(",")
            if busca[0] == nombre:
                if not busca[5]:
                    if bool(sl2[0] in busca[1] )==True:
                        if bool(sl2[1] in busca[1])==True:
                            if bool(sl[1] in busca[2])==True:
                                busca[5].append(transicion1)
                                banderatransi=True
                                auxiliar1+='EMPTY -> '+busca[3][0]+' [ label = "" ];\n'
                                auxdfagraph+=''+sl2[0]+' -> '+sl2[1]+' [ label = "'+sl[1]+'" ];\n'
                            elif bool(sl[1] in busca[2])==False:
                                 print("El "+sl[1]+" no existe en la lista de Alfabetos") 
                        elif bool(sl2[1]in busca[1])==False:
                            print("El "+sl2[1]+" no existe en la lista de estados")
                    elif bool(sl2[0] in busca[1])==False:
                            print("El "+sl2[0]+" no existe en la lista de estados")   
                elif busca[5]:
                    if transicion1 in busca[5]:
                        print("Error las transiciones no pueden repetirse, Las transiciones repetidas solo son aceptadas en AFN")
                    else:
                        if bool(sl2[0] in busca[1] )==True:
                            if bool(sl2[1] in busca[1])==True:
                                if bool(sl[1] in busca[2])==True:
                                    busca[5].append(transicion1)
                                    banderatransi=True
                                    auxdfagraph+=''+sl2[0]+' -> '+sl2[1]+' [ label = "'+sl[1]+'" ];\n'
                                elif bool(sl[1] in busca[2])==False:
                                    print("El "+sl[1]+" no existe en la lista de Alfabetos") 
                            elif bool(sl2[1]in busca[1])==False:
                                print("El "+sl2[1]+" no existe en la lista de estados")
                        elif bool(sl2[0] in busca[1])==False:
                            print("El "+sl2[0]+" no existe en la lista de estados")
                      
    menupreg()                            
def modo2(pase,nombre):
    global lista,auxiliar1,auxdfagraph, banderatransi
    auxi=''
    auxi2=''
    #auxiliar2=str(input("Ingrese las transiciones de las siguiente manera [estado 1,estado 2; estado 1,estado 2]:\n"))
    auxiliar2=pase
    strange=auxiliar2.split("[")
    strange1=strange[1].split("]")
    strange2=strange1[0].split(";")
    if auxiliar2== '' or auxiliar2=='\t' or auxiliar2==' ':
        modo2()
    else:
        for busca in lista:
            if busca[0]== nombre:
                
                    #for lista2 in strange2:
                        x=0
                        while x<int(len(strange2)):
                            bandera2=False
                            strange3=strange2[x].split(",") 
                            #for i in  strange3:
                            k=0
                            while k < int(len(strange3)):   
                                if not busca[5]:
                                    if bool(strange3[k] in busca[1])==True:
                                        bandera=False
                                        z=0
                                        while z<int(len(busca[1])) and  bandera==False :
                                    
                                                if busca[1][z]==strange3[k] :
                                                    bandera =True
                                                    if bandera2==False:
                                                        aux=busca[1][x]
                                                        bandera2=True
                                                z+=1
                                        if bandera==True:
                                            dato=strange3[k]
                                            num=strange3.index(dato)
                                            auxi=''+aux+','+strange3[k]+';'+busca[2][k]
                                            busca[5].append(auxi)
                                            banderatransi=True
                                            auxiliar1+='EMPTY -> '+busca[3][0]+' [ label = "" ];\n'
                                            auxdfagraph+=''+aux+' -> '+strange3[k]+' [ label = "'+busca[2][k]+'" ];\n'
                                        
                                    elif bool(strange3[k] in busca[1])==False:        
                                        bandera=False
                                        z=0
                                        while z<int(len(busca[1])) and  bandera==False:
                                    
                                                if strange3[k]=='-' or strange3[k]==''or strange3[k]==' ':
                                                    bandera =True
                                                    if bandera2==False:
                                                        aux=busca[1][x]
                                                        bandera2=True
                                                       
                                                z+=1
                                        if bandera==True:
                                            #dato=strange3[k]
                                            #num=strange3.index(dato)
                                            auxi=''+aux+','+strange3[k]+';'+busca[2][k]
                                            busca[5].append(auxi) 
                                elif busca[5]:
                                    if bool(strange3[k] in busca[1])==True:
                                        bandera=False
                                        z=0
                                        while z<int(len(busca[1])) and  bandera==False:
                                    
                                                if busca[1][z]==strange3[k]:
                                                    bandera =True
                                                    if bandera2==False:
                                                        aux=busca[1][x]
                                                        bandera2=True
                                                z+=1
                                        if bandera==True:
                                            #dato=strange3[k]
                                            #num=strange3.index(dato)
                                            auxi=''+aux+','+strange3[k]+';'+busca[2][k]
                                            busca[5].append(auxi)
                                            banderatransi=True
                                            auxdfagraph+=''+aux+' -> '+strange3[k]+' [ label = "'+busca[2][k]+'" ];\n'
                                        
                                    elif bool(strange3[k] in busca[1])==False:        
                                        bandera=False
                                        z=0
                                        while z<int(len(busca[1])) and  bandera==False :
                                    
                                                if strange3[k]=='-' or strange3[k]==''or strange3[k]==' ':
                                                    bandera =True
                                                    if bandera2==False:
                                                        aux=busca[1][x]
                                                        bandera2=True
                                                       
                                                z+=1
                                        if bandera==True:
                                            #dato=strange3[k]
                                            #num=strange3.index(dato)
                                            auxi=''+aux+','+strange3[k]+';'+busca[2][k]
                                            busca[5].append(auxi)
                                k+=1                          
                            x+=1
                        
    menupreg() 
                        
def preginicio(inicial):
    global lista,nombre
    toctoc=inicial
    for buscar in lista:
        if buscar[0]==nombre:
            inicial1=str(input("esta seguro de querer modificar Estado Inicial? presiona (y) para continuar y (N) para regresar al menu AFD :\n"))
            if inicial1 =='y' or inicial1 =='Y':
                buscar[3].insert(3,str(inicial))
            if inicial1 =='N' or inicial1 =='n':
                os.system("cls")
                menuAFD()
            else:
                preginicio(toctoc)

def menumodo():
    global banderamenu
    opcional=0
    while opcional != 3:
        os.system("cls") 
        print("!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!\t 1. Modo1 \t!")
        print("!\t 2. Modo2 \t!")
        print("!\t 3. salir \t!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!")
        opcional = str(input("Ingrese la Opcion:\n"))
        if opcional== '1':
            banderamenu=5
            modo1()
        
        elif opcional == '2':
            banderamenu=6
            modo2()
        
        elif opcional == '3':
            menuAFD()        
        else:
            menumodo()
def menupreg():
    global auxiliar1,dfagraph,auxdfagraph,nombre,banderamenu
    if banderamenu==1:
        pregunta= str(input("¿Deseas agregar un Estado mas? presiona (y) para continuar y (N) para regresar al menu AFD :\n"))
        if pregunta=='y' or pregunta =='Y':
            estados()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
        else:
            menupreg()    
    elif banderamenu==2:
        pregunta= str(input("¿Deseas agregar un Alfabeto mas? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            alfabetos()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
        else:
            menupreg()
    elif banderamenu == 3:
        pregunta = str(input("¿Deseas modificar el Estado Inicial ? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            inicialstate()
        elif pregunta =='N' or pregunta =='n':
            if banderatransi==True:
                unir=dfagraph+auxiliar1+auxdfagraph+'}'
                graph.grafic(unir,nombre)
                os.system("cls")
                menuAFD()
            else:   
                os.system("cls")
                menuAFD()
        else:
            menupreg()    
    elif banderamenu==4:
        pregunta = str(input("¿Deseas ingresar mas estados de aceptacion? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            finalstate()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
        else:
            menupreg()
    elif banderamenu== 5:  
        pregunta = str(input("¿Deseas ingresar mas transiciones? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            modo1()
        elif pregunta =='N' or pregunta =='n':
            if banderatransi==True:
                unir=dfagraph+auxiliar1+auxdfagraph+'}'
                graph.grafic(unir,nombre)
                os.system("cls")
                menuAFD()
            else:   
                os.system("cls")
                menuAFD()
        else:
            menupreg()      
    elif banderamenu==6:  
        pregunta = str(input("¿Deseas ingresar mas transiciones? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            modo2()
        elif pregunta =='N' or pregunta =='n':
            if banderatransi==True:
                unir=dfagraph+auxiliar1+auxdfagraph+'}'
                graph.grafic(unir,nombre)
                os.system("cls")
                menuAFD()
            else:   
                os.system("cls")
                menuAFD()
        else:
            menupreg()    
    else:
        menupreg()                       
pedirnombre()
#inicialstate()
#modo2()

    
