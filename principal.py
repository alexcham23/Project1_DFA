import msvcrt
import menu
import os
def caratula():
    print("*********************************************************")
    print("*\t Lenguajes Formales de programación\t\t*")
    print("*\t\t\tSeccion: A-\t\t\t*")
    print("*\t\t\t 201602983\t\t\t*")
    print("*********************************************************")

def press_enter():
    while True:
        print("Presione enter para continuar ")
        m= str(msvcrt.getch(),'utf -8')
        if m == "\r":
            menu.prueba()
            break
      

def menuprin():
    
    caratula()
    press_enter()
      
menuprin()