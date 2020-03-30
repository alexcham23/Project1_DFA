import os

lista2=[]
NT=[]
nombre=""
Terminales=[]
inicialNT=[]
Producciones=[]
original=[]
banderaestado=False
banderamenu=False
auxiliar1=''
banderatransi=False
estadoA=[]
estadoB=[]
NOT=[]
evalcadenas=[]
def menuAFD():
    global banderamenu,banderaestado
    op = 0
    while op != 8:
        print("=========================================================")
        print("=\t\t 1.   Ingresar No Terminales\t\t\t=") 
        print("=\t\t 2.   Ingresar terminales\t\t\t=") 
        print("=\t\t 3.   No terminal Inicial\t\t\t=") 
        print("=\t\t 4.   Producciones\t\t=")
        print("=\t\t 5.   Mostrar Gramatica Transformada \t\t\t=") 
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
                print("por favor ingrese de primero los No Terminales\n")
                menuAFD()     
           
            break
        elif op == '3' :
            if(banderaestado==True):
                banderamenu=3
                inicialstate()
            else:
                os.system("cls")
                print("por favor ingrese de primero los No Terminales\n")
                menuAFD() 
            break
        elif op == '4' :
            if(banderaestado==True):
                banderamenu=3
                producciones()
            else:
                os.system("cls")
                print("por favor ingrese de primero los No Terminales\n")
                menuAFD() 
            break
        elif op == '5' :
            if(banderaestado==True):
                banderamenu=3
                mostrar()
            else:
                os.system("cls")
                print("por favor ingrese de primero los No Terminales\n")
                menuAFD() 
            break
        elif op == '6' :
            banderamenu=6
            break
        else:
            menuAFD()
def pedirnombre():
    global NT,Terminales,inicialNT,Producciones,lista2,evalcadenas,NOT,estadoA,estadoB
    nombre2= str(input("Ingrese el nombre de la gramatica:\n "))
    if nombre2=="" or nombre2=="\t":
        os.system("cls")
        pedirnombre()
    else:    
        guardar=nombre2,NT,Terminales,inicialNT,Producciones,original
        lista2.append(guardar)
        guardar2=nombre2,estadoA,NOT,estadoB
        evalcadenas.append(guardar2) 
        dfagraph="digraph \""+nombre+"\" {\n"
        dfagraph+="rankdir=LR;\nsize=\"42,42\"  EMPTY [style=invis]  EMPTY [shape=point] node [shape = doublecircle];\n"
        menuAFD()
        #imprimir()           
def estados():
    global nombre,lista2,banderaestado
   
    estado= str(input("Ingrese el no terminal:\n"))
    banderaestado=True
    bandera = False
    if estado=="" or estado=="\t":
        os.system("cls")
        estados()
    else:   
        for busca in lista2:
            if busca[0] == nombre:
                x=0
                if not busca[1]:#verificamos si lista de estados esta vacia
                    busca[1].append(estado)
                
                elif busca[1]:# de caso contrario no esta vacia    
                    while x < int(len(busca[1])) and bandera ==False:# verificamos el tamaño de la lista estado
                        if busca[1][x] == estado:# verificamos si existe un estado repetido
                            print("este No Terminal ya existe") 
                            bandera = True
                        x+=1    
                     
                    if bandera== False:#guardamos el estado si no se encuentra repetido
                        busca[1].append(estado)
    menupreg()                      
                        
def alfabetos():
    global nombre,lista2
    bandera1=False
    bandera2=False
    alfabeto=str(input("Ingrese el Terminal:\n"))
    if alfabeto=="" or alfabeto=="\t":
        os.system("cls")
        alfabeto()
    else:
        for busca in lista2:
            if busca[0]==nombre:
                if not busca[2]: #lista de la columna 2 esta vacia  
                    x=0
                    while x < int(len(busca[1])) and bandera1==False :
                        if busca[1][x]==alfabeto:
                            print("EL terminal "+alfabeto+" debe de ser diferente a los NO TERMINALES")
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
                            print("EL terminal "+alfabeto+" debe de ser diferente a los NO TERMINALES")    
                    elif bool(alfabeto in busca[2])==True:
                        print("El terminal "+alfabeto+" ya existe en la Base de datos")  
    menupreg()             
def inicialstate():
    global lista2,nombre,auxiliar1
    bandera =False
    iniciales = str(input("Ingrese el estado inicial:\n"))
    if iniciales =="" or iniciales=="\t":
        os.system("cls")
        inicialstate()
    else:
        for buscar in lista2:
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
def producciones(master,nombre): 
    global lista2#nombre  
    separa=[]
    verifica1=''
    verifica2=''
    verifica3=''
    recur=''
    banderafinal = False
    banderaguardar = False
    prod=str(master)#str(input('Ingrese las produciones:\n'))
    nueva=prod.replace(" ", "")
    print(nueva)
    if prod=="" or prod=="\t":
        os.system("cls")
        producciones()
    else:                  
        for busca in lista2:
            busca[5].append(prod)  
            if busca[0]== nombre: 
                #busca[5].append(prod) 
                for val in evalcadenas:            
                    if val[0]==nombre:
                        dato=nueva.split(">")
                #if not busca[4]:
                        if bool(dato[0] in busca[1])==True:
                            dato2=dato[1].split("|")
                            for i in range(len(dato2)): 
                                    for letra in dato2[i]:
                                            if bool(letra in busca[1])==True:
                                                verifica1=letra
                                            elif bool(letra in busca[2])==True:
                                                verifica2=letra
                                                 
                                            else:
                                                verifica3+=letra 
                                                banderafinal=True 
                                    if verifica3=="epsilon" and banderafinal == True:
                                        recur=dato[0]+' > '+verifica3+''
                                        banderaguardar=True
                                    elif verifica3 !="epsilon" and banderafinal==True:
                                        verifica3=""
                                        banderafinal=False
                                    else:            
                                        recur=dato[0]+' > '+verifica2+''+verifica1    
                                    if not busca[4]:
                                        if verifica3=="epsilon" and banderaguardar==True:
                                            busca[4].append(recur)
                                            val[1].append(dato[0])
                                            val[2].append(verifica3)
                                            val[3].append('')
                                            #verifica3=""
                                        else:    
                                            busca[4].append(recur)
                                            val[1].append(dato[0])
                                            val[2].append(verifica2)
                                            val[3].append(verifica1)
                                            
                                            verifica3=""
                                    elif busca[4]:     
                                        if bool(recur in busca[4])==False:
                                            if verifica3=="epsilon" and banderaguardar==True:
                                                busca[4].append(recur)
                                                val[1].append(dato[0])
                                                val[2].append(verifica3)
                                                val[3].append('')
                                                banderaguardar==False
                                                verifica3=""
                                            else:
                                                busca[4].append(recur)
                                                val[1].append(dato[0])
                                                val[2].append(verifica2)
                                                val[3].append(verifica1)
                                                verifica3=""
                                 
                                           
                    elif bool(dato[0] in busca[1])==False:  
                        print("Error NT o  el terminal no existe")
         
        menupreg()              
def mostrar():
    global lista2,nombre
    muestra1='Gramatica Original\n'
    muestra2='Gramatica sin recusividad por la Izquierda\n'
    for busca in lista2:
        if busca[0]==nombre:
            for i in busca[5]:
                muestra1+=i+'\n'
            for i in busca[4]:   
                muestra2+=i+'\n'
                             
    print(muestra1)
    print(muestra2)
def menupreg():
    global auxiliar1,nombre,banderamenu
    if banderamenu==1:
        pregunta= str(input("¿Deseas agregar No terminales? presiona (y) para continuar y (N) para regresar al menu AFD :\n"))
        if pregunta=='y' or pregunta =='Y':
            estados()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
        else:
            menupreg()    
    elif banderamenu==2:
        pregunta= str(input("¿Deseas agregar un terminal? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            alfabetos()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
        else:
            menupreg()
    elif banderamenu == 3:
        pregunta = str(input("¿Deseas modificar el NT Inicial ? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            inicialstate()
        elif pregunta =='N' or pregunta =='n':
            if banderatransi==True:
                #unir=dfagraph+auxiliar1+auxdfagraph+'}'
               # graph.grafic(unir,nombre)
                os.system("cls")
                menuAFD()
            else:   
                os.system("cls")
                menuAFD()
        else:
            menupreg()    
    elif banderamenu==4:
        pregunta = str(input("¿Deseas ingresar mas producciones? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            producciones()
        elif pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
        else:
            menupreg()
    elif banderamenu== 5:  
        pregunta = str(input("¿Deseas ingresar mas transiciones? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
           # modo1()
           mostrar()
        elif pregunta =='N' or pregunta =='n':
            if banderatransi==True:
               # unir=dfagraph+auxiliar1+auxdfagraph+'}'
               # graph.grafic(unir,nombre)
                os.system("cls")
                menuAFD()
            else:   
                os.system("cls")
                menuAFD()
        else:
            menupreg()      
    elif banderamenu==6:  
        print()
           
    else:
        menupreg()                        
def simulacion():
    global lista2,nombre,NT,Terminales,inicialNT,Producciones,original
    guardar='master',NT,Terminales,inicialNT,Producciones,original
    lista2.append(guardar)
    guardar2='master',estadoA,NOT,estadoB
    evalcadenas.append(guardar2) 
    for busca in lista2:
         
         busca[1].append('A')
         busca[1].append('B')
         busca[1].append('C')
         busca[1].append('D')
         busca[2].append('0')
         busca[2].append('1')
         busca[3].append('A')
    producciones('A > 0B | 1A | epsilon','master')
    
simulacion()