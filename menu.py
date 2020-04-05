
import sys
import os
import AFD
import gramatica
import Archivo
def retorno():
    prueba()
def prueba():
    op = 0
    while op != 6:
        print ("*************************************************")
        print("*\t 1. Crear AFD \t\t\t\t*")
        print("*\t 2. Crear Gramatica     \t\t*")
        print("*\t 3. Evaluar Cadenas     \t\t*")
        print("*\t 4. Reportes \t\t\t\t*")
        print("*\t 5. Cargar Archivo de Entrada   \t*")
        print("*\t 6. Salir \t\t\t\t*")
        print("*************************************************")
        op = str(input("Elige una opcion:\n"))       

        if op == '1' :
            os.system("cls")
            AFD.pedirnombre()
            break
        elif op == '2' :
            os.system("cls")
            gramatica.pedirnombre()
            break
        elif op == '3' :
            os.system("cls")
            gramatica.valinombre()
            break
        elif op == '4' :
            print()
            break
        elif op == '5' :
            os.system("cls")
            Archivo.menuarchivo()
            break
        elif op == '6' :
            sys.exit()
            break

#prueba()