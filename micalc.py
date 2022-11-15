#creo la interface para la calculadora
from tkinter import *
#creo la ventana
ventana = Tk()
ventana.title("calculadora")
ventana.geometry("400x400")
#ventana.config(bg="black")
#creo las variables
n1 = StringVar()
n2 = StringVar()
resultado = StringVar()
#creo las funciones
def sumar():
    resultado.set(float(n1.get()) + float(n2.get()))
    borrar()
def restar():
    resultado.set(float(n1.get()) - float(n2.get()))
    borrar()
def multiplicar():
    resultado.set(float(n1.get()) * float(n2.get()))
    borrar()
def dividir():
    resultado.set(float(n1.get()) / float(n2.get()))
    borrar()
def borrar():
    n1.set("")
    n2.set("")
#creo los labels
Label(ventana, text="numero 1", bg="black", fg="white").place(x=10, y=10)
Label(ventana, text="numero 2", bg="black", fg="white").place(x=10, y=40)
Label(ventana, text="resultado", bg="black", fg="white").place(x=10, y=70)
#creo los entry
Entry(ventana, textvariable=n1).place(x=100, y=10)
Entry(ventana, textvariable=n2).place(x=100, y=40)
Entry(ventana, textvariable=resultado, state="disabled").place(x=100, y=70)
#creo los botones
Button(ventana, text="sumar", command=sumar).place(x=10, y=100)
Button(ventana, text="restar", command=restar).place(x=60, y=100)
Button(ventana, text="multiplicar", command=multiplicar).place(x=110, y=100)
Button(ventana, text="dividir", command=dividir).place(x=180, y=100)
Button(ventana, text="borrar", command=borrar).place(x=230, y=100)
ventana.mainloop()

