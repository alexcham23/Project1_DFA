from gramatica import lista2
import os
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
cadenasvali=[]
cadenasinva=[]
ruta=[]
expandir=[]
inicio=''
evalcadenas=[]
def pedirnombre(nombr):
    global NT,Terminales,inicialNT,Producciones,lista2,evalcadenas,NOT,estadoA,estadoB,nombre
    nombre=nombr
    if nombre !="" or nombre!="\t" :
        guardar=nombre,NT,Terminales,inicialNT,Producciones,original
        lista2.append(guardar)
        guardar2=nombre,estadoA,NOT,estadoB,cadenasvali,cadenasinva,ruta,expandir 
        evalcadenas.append(guardar2) 
        dfagraph="digraph \""+nombre+"\" {\n"
        dfagraph+="rankdir=LR;\nsize=\"42,42\"  EMPTY [style=invis]  EMPTY [shape=point] node [shape = doublecircle];\n"
        #menuAFD()
        #imprimir()          
def estados(NT):
    global nombre,lista2,banderaestado
   
    estado=NT
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
def alfabetos(terminales):
    global nombre,lista2
    bandera1=False
    bandera2=False
    alfabeto=terminales
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
def inicialstate(inicial):
    global lista2,nombre,auxiliar1
    bandera =False
    iniciales = inicial
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
def producciones(prodi,obten): 
    global lista2,evalcadenas,nombre  
    separa=[]
    verifica1=''
    verifica2=''
    verifica3=''
    recur=''
    banderafinal = False
    banderaguardar = False
    prod=prodi
    nueva=prod.replace(" ", "")
    print(nueva)
    if prod=="" or prod=="\t":
        os.system("cls")
        producciones()
    else:  
        dat=" "
        if bool(dat in prod)==True:                
            for busca in lista2:
                busca[5].append(obten)  
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
                                            banderafinal=False
                                            banderafinal=False
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
                                                banderaguardar=False
                                                banderafinal=False
                                                verifica3=""
                                            else:
                                                busca[4].append(recur)
                                                val[1].append(dato[0])
                                                val[2].append(verifica2)
                                                val[3].append(verifica1)
                                                verifica3=""
                                 
                                           
                        elif bool(dato[0] in busca[1])==False:  
                            print("Error NT o  el terminal no existe")
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