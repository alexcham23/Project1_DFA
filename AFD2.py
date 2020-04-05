from AFD import lista
import os
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
dfagraph=""
auxdfagraph=""
auxiliar1='node [shape = circle];\n'
def pedirnombre(nr):
    global nombre,estado,alfabeto,inicial,aceptacion,transiciones,lista,dfagraph
    nombre =nr
    if nombre!="" or nombre!="\t":
        guardar=nombre,estado,alfabeto,inicial,aceptacion,transiciones
        lista.append(guardar)
        dfagraph="digraph \""+nombre+"\" {\n"
        dfagraph+="rankdir=LR;\nsize=\"42,42\"  EMPTY [style=invis]  EMPTY [shape=point] node [shape = doublecircle];\n"
    print(lista) 
def estados(est):
    global nombre,lista,banderaestado
   
    estado= est
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
def alfabetos(alf):
    global nombre,lista
    bandera1=False
    bandera2=False
    alfabeto=alf
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
def inicialstate(inicio):
    global lista,nombre,auxiliar1
    bandera =False
    iniciales = inicio
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
def finalstate(final):
    global lista,nombre,dfagraph
    bandera =False
    iniciales = final
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
def modo1(crear):
    global lista,nombre,banderatransi,auxiliar1,auxdfagraph
    transicion1=crear
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
