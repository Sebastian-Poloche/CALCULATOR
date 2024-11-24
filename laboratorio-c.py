import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.iconbitmap("pepe-el-pollo.ico")
ventana.resizable(width=False, height=False)
ventana.geometry("+580+130")

# labels de la linea de la calculadora

datos1 = tk.StringVar()
Labeldatos1 = tk.Label(ventana, textvariable=datos1, width=4, height=1, font="calibri 9", anchor="e")
Labeldatos1.grid(row=0, column=0, columnspan=4, sticky="w,e")

datos2 = tk.StringVar()
Labeldatos2 = tk.Label(ventana, textvariable=datos2, width=4, height=2, font="calibri 20", anchor="e")
Labeldatos2.grid(row=1, column=0, columnspan=4, sticky="w,e")

# botones de la calculadora

# #linea 1

botonAC = tk.Button(ventana, text="AC", width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: borrar_todo())
botonAC.grid(row=2, column=0)

botonR = tk.Button(ventana, text=chr(9003), width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: borrar_uno())
botonR.grid(row=2, column=1)

botonRaizcuadrada = tk.Button(ventana, text="√", width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: raizcuadrada())
botonRaizcuadrada.grid(row=2, column=2)

botondivision = tk.Button(ventana, text=chr(247), width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: funcion_botones("/"))
botondivision.grid(row=2, column=3)

# linea 2

boton7 = tk.Button(ventana, text="7", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("7"))
boton7.grid(row=3, column=0)

boton8 = tk.Button(ventana, text="8", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("8"))
boton8.grid(row=3, column=1)

boton9 = tk.Button(ventana, text="9", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("9"))
boton9.grid(row=3, column=2)

botonmultiplicacion = tk.Button(ventana, text="x", width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: funcion_botones("*"))
botonmultiplicacion.grid(row=3, column=3)

# linea 3

boton4 = tk.Button(ventana, text="4", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("4"))
boton4.grid(row=4, column=0)

boton5 = tk.Button(ventana, text="5", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("5"))
boton5.grid(row=4, column=1)

boton6 = tk.Button(ventana, text="6", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("6"))
boton6.grid(row=4, column=2)

botonresta = tk.Button(ventana, text="-", width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: funcion_botones("-"))
botonresta.grid(row=4, column=3)

# linea 4

boton1 = tk.Button(ventana, text="1", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("1"))
boton1.grid(row=5, column=0,)

boton2 = tk.Button(ventana, text="2", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("2"))
boton2.grid(row=5, column=1)

boton3 = tk.Button(ventana, text="3", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("3"))
boton3.grid(row=5, column=2)

botonsuma = tk.Button(ventana, text="+", width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: funcion_botones("+"))
botonsuma.grid(row=5, column=3)

# linea 5

botoncero = tk.Button(ventana, text="0", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("0"))
botoncero.grid(row=6, column=0)

botonpunto = tk.Button(ventana, text=".", width=7, height=3, bg="gray", fg="white", border=3, relief="raised", command=lambda: funcion_botones("."))
botonpunto.grid(row=6, column=1)

botonigual = tk.Button(ventana, text="=", width=7, height=3, bg="blue", fg="white", border=3, relief="raised", command=lambda: funcion_botones("="))
botonigual.grid(row=6, column=2, columnspan=2, sticky="w,e")

# espacios entre botones

for espacios in ventana.winfo_children():
    espacios.grid_configure(ipady=1, padx=1, pady=1)

# funciones para los botones

    def funcion_botones(tecla):
        if tecla >= "0" and tecla <= "9" or tecla == ".":
            datos2.set(datos2.get() + tecla)

# funcion para las expresiones matematicas

        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            if tecla == "*":
                datos1.set(datos2.get() + "*")
            elif tecla == "/":
                datos1.set(datos2.get() + "/")
            elif tecla == "+":
                datos1.set(datos2.get() + "+")
            elif tecla == "-":
                datos1.set(datos2.get() + "-")

# para al dar enviar los primeros digitos al Label1 se limpie el Label2

            datos2.set("")
    
# funcion para dar el resultado

        if tecla == "=":
            datos1.set(datos1.get() + datos2.get())
            resultado = eval(datos1.get())
            datos2.set(resultado)

# funcion para la raiz cuadrada

def raizcuadrada():
    datos1.set("")
    resultado = math.sqrt(float(datos2.get()))
    datos2.set(resultado)

# funcion para borrar de uno en uno

def borrar_uno():
    inicio = 0
    final = len(datos2.get())

    datos2.set(datos2.get()[inicio:final-1])

# funcion para borrar todo

def borrar_todo():
    datos1.set("")
    datos2.set("")

# funcion de ventana final

ventana.mainloop()