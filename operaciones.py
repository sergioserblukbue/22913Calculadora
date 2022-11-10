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