nombre=estado=alfabeto=inicial=final=aceptacion=transiciones=""
lista= list()
def menuAFD():
    op = 0
    while op != 7:
        print("=========================================================")
        print("=\t\t 1.   Ingresar Estados\t\t\t=") 
        print("=\t\t 2.   Ingresar Alfabeto\t\t\t=") 
        print("=\t\t 3.   Estado Inicial\t\t\t=") 
        print("=\t\t 4.   Estado de Aceptacion\t\t=")
        print("=\t\t 5.   Transiciones \t\t\t=") 
        print("=\t\t 6.   Ayuda\t\t\t=")
        print("=\t\t 7.   Menu Principal\t\t\t=") 
        print("=========================================================")
        op = str(input("Elige una opcion:\n"))       

        if op == '1' :
            
            break
        elif op == '2' :
           
            break
        elif op == '3' :
           
            break
        elif op == '4' :
           
            break
        elif op == '5' :
           
            break
        elif op == '6' :
            
            break
        elif op == '7' :
            print("hola")
            break
def pedirnombre():
    global nombre,estado,alfabeto,inicial,final,aceptacion,transiciones,lista
    nombre= str(input("Ingrese Un nombre para el AFD:\n "))
    guardar=nombre,estado,alfabeto,inicial,final,aceptacion,transiciones
    lista.append(guardar)
    menuAFD()
    imprimir()
def imprimir():
    global lista
    for x in lista:
        print(x)
pedirnombre()