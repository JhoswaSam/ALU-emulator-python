import tkinter as tk

def btn_click(numbers):

    global operador
    operador=operador + str(numbers)
    var.set(operador)

def btn_clear_display():

    global operador
    operador=""
    var.set(operador)

def btn_equals_input():
    global operador
    try:
        sumup=str(eval(operador))
    except ZeroDivisionError:
        operador="0"
        var.set(operador)
        operador = ""
    else:
        var.set(sumup)  
        operador = sumup

def btn_erase():
    global operador
    operador = operador[:temp - 1]
    var.set(operador)

ventana = tk.Tk()
ventana.title("")
ventana.geometry('215x250')

operador=""
var = tk.StringVar()

temp = len(operador)


display = tk.Label(ventana, bg = "white" ,textvariable = var, width = 20).place(x = 20, y = 20)

b1 = tk.Button(ventana, text = "1", command=lambda:btn_click(1), fg = "black", width = 1).place(x = 20, y = 80)
b2 = tk.Button(ventana, text = "2", command=lambda:btn_click(2), fg = "black", width = 1).place(x = 55, y = 80)
b3 = tk.Button(ventana, text = "3", command=lambda:btn_click(3), fg = "black", width = 1).place(x = 90, y = 80) 
b4 = tk.Button(ventana, text = "4", command=lambda:btn_click(4), fg = "black", width = 1).place(x = 20, y = 115)
b5 = tk.Button(ventana, text = "5", command=lambda:btn_click(5), fg = "black", width = 1).place(x = 55, y = 115)
b6 = tk.Button(ventana, text = "6", command=lambda:btn_click(6), fg = "black", width = 1).place(x = 90, y = 115)
b7 = tk.Button(ventana, text = "7", command=lambda:btn_click(7), fg = "black", width = 1).place(x = 20, y = 150)
b8 = tk.Button(ventana, text = "8", command=lambda:btn_click(8), fg = "black", width = 1).place(x = 55, y = 150)
b9 = tk.Button(ventana, text = "9", command=lambda:btn_click(9), fg = "black", width = 1).place(x = 90, y = 150)
b0 = tk.Button(ventana, text = "0", command=lambda:btn_click(0), fg = "black", width = 1).place(x = 55, y = 185)

boton_suma = tk.Button(ventana, text = "+", command=lambda:btn_click("+"), fg = "black", width = 2).place(x = 130, y = 80)
boton_resta = tk.Button(ventana, text = "-", command=lambda:btn_click("-"), fg = "black", width = 2).place(x = 155, y = 80)
boton_multi = tk.Button(ventana, text = "x", command=lambda:btn_click("*"), fg = "black", width = 2).place(x = 130, y = 115)
boton_divi = tk.Button(ventana, text = "/", command=lambda:btn_click("/"), fg = "black", width = 2).place(x = 155, y = 115)
boton_elevar = tk.Button(ventana, text = "elevar", command=lambda:btn_click("**"), fg = "black", width = 5).place(x = 130, y = 150)
boton_equals = tk.Button(ventana, text = "=", command=btn_equals_input, fg = "black", width = 5).place(x = 130, y = 185)
boton_clear = tk.Button(ventana, text = "C", command=btn_clear_display, fg = "black", width = 1).place(x = 20, y = 185)
boton_erase = tk.Button(ventana, text = "<--", command=btn_erase, fg = "black", width = 1).place(x = 90, y = 185)       

ventana.mainloop()