import os
#  creo las funciones para las operaciones
def sumar(n1,n2):
    return n1 + n2
def restar(n1, n2):
    return n1-n2
def multiplicar(n1, n2):
    return n1*n2
def dividir(n1,n2):
    try:
        return n1/n2
    except:
        print("no se puede dividir por cero ")

# funcion para el menu
def menu():
    os.system("cls")
    print("+ prara sumar")
    print("- para restar")
    print("/ para dividir")
    print("* para Multiplicar")
    print("s para salir")

# funcion principal
def main():
    menu()
    op=input("ingrese una operación ")
    while op != "s":
        pn=int(input("ingrese un numero: "))
        sn=int(input("ingrese otro numero: "))
        if op=="+":
            print("el resultado de la suma es:" , sumar(pn,sn)) 
        elif op =="-":
            print ("el resultado de la resta es: ",  restar(pn,sn))
        elif op=="/":
            print("el resultado de la división es: ", dividir(pn, sn))
        elif op=="*":
            print ("")
        else:
            print("opcion no valida")
        op=input("ingrese una operación ")

# aca empieza el programa
main()





