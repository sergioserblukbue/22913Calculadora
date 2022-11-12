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
def potencia():
    n=int(input("ingrese el numero a elevar: "))
    x=int (input("ingrese la ponencia: "))
    i=1
    r=n
    while (i<x):
        r= r * n
        i=i+1

    return r