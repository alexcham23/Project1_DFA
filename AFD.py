import os
nombre=""
estado=[]
alfabeto=[]
inicial=[]
final=[]
aceptacion=[]
transiciones=[]
banderamenu= 0
banderaestado=False
lista=[]
dfagraph=""
auxdfagraph=""
def menuAFD():
    global banderamenu,banderaestado
    op = 0
    while op != 7:
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
            banderamenu=2
            break
        elif op == '5' :
           
            break
        elif op == '6' :
            
            break
        elif op == '7' :
            print("hola")
            break
def pedirnombre():
    global nombre,estado,alfabeto,inicial,final,aceptacion,transiciones,lista,dfagraph
    nombre= str(input("Ingrese Un nombre para el AFD:\n "))
    guardar=nombre,estado,alfabeto,inicial,final,aceptacion,transiciones
    lista.append(guardar)
    dfagraph+="digraph \""+nombre+"\" {\n"
    dfagraph+="rankdir=LR;\nsize=\"42,42\"  EMPTY [style=invis]  EMPTY [shape=point] node [shape = doublecircle];"
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
    for busca in lista:
        if busca[0] == nombre:
            x=0
            if not busca[1]:#verificamos si lista de estados esta vacia
                busca[1].append(estado)
                
            elif busca[1]:# de caso contrario no esta vacia    
                while x < int(len(busca[1])) and bandera ==False:# verificamos el tamaño de la lista estado
                    if busca[1][x] == estado:# verificamos si existe un estado repetido
                        print("este Estado Y existe") 
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
                            print("EL alfabeto "+alfabeto+" debe de ser diferente al nombre del estado")
                            bandera1=True
                        y+=1
                    if bandera1== False:
                        busca[2].append(alfabeto)
                elif bool(alfabeto in busca[2])==True:
                    print("El alfabeto "+alfabeto+" ya existe en la Base de datos")  
    menupreg()
def inicialstate():
    global lista,nombre
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
                        
                elif buscar[3]:
                    y=0
                    while y <int(len(buscar[1])) and bandera == False: 
                        if buscar[1][y] == iniciales:
                            bandera = True
                        y+=1
                    if bandera == True:
                        buscar[3].insert(0,iniciales)
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

def menupreg():
    if banderamenu==1:
        pregunta= str(input("¿Deseas agregar un Estado mas? presiona (y) para continuar y (N) para regresar al menu AFD :\n"))
        if pregunta=='y' or pregunta =='Y':
            estados()
        if pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
    elif banderamenu==2:
        pregunta= str(input("¿Deseas agregar un Alfabeto mas? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            alfabetos()
        if pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
    elif banderamenu == 3:
        pregunta = str(input("¿Deseas modificar el Estado Inicial ? presiona (y) para continuar y (N) para regresar al menu AFD : \n"))
        if pregunta=='y' or pregunta =='Y':
            inicialstate()
        if pregunta =='N' or pregunta =='n':
            os.system("cls")
            menuAFD()
    else:
        menupreg()                       
pedirnombre()
#inicialstate()
