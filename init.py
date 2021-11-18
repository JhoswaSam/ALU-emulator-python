import tkinter as tk
from tkinter import *
from tkinter import ttk 

def retrieve_input():
    inputValue=text.get("1.0","end-1c")
    print(inputValue)

def btn_click(numbers):
    global operador
    operador=operador + str(numbers)
    var.set(operador)

def btn_equals_input():
    global operador
    try:
        sumup=str(eval(operador))
    except ZeroDivisionError:
        operador="0"
        var_decimal.set(operador)
        operador = ""
    else:
        var_decimal.set(sumup)  
        operador = sumup
        btn_clear_display()

def btn_erase():
    global operador
    operador = operador[:temp - 1]
    var.set(operador)

def btn_clear_display():

    global operador
    operador=""
    var.set(operador)

def btn_clear_all():
    global operador
    operador=""
    var_binario.set(operador)
    var_decimal.set(operador)
    var_hexadecimal.set(operador)
    var_octal.set(operador)

class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)



root = tk.Tk()
root.config(width=700, height=380)
root.title("ALU simulator")

operador=""
temp = len(operador)
var = tk.StringVar()
tk.Label(root, bg = "white" ,textvariable = var, width =26).place(x = 40, y = 30)


#
#       INSERT BUTTON NUMBER
#

buttons = [1,2,3,4,5,6,7,8,9,"+",0,"-","*","/"]
x_position_number = 40
y_position_number = 110
for i, b in enumerate(buttons):
    if( (i+1) % 3 != 0):
        Button(root,height=1,width=1,text=b, command=Callback(btn_click, b)).place(x= x_position_number,y=y_position_number)
        x_position_number += 89
    else:
        Button(root,height=1,width=1,text=b, command=Callback(btn_click, b)).place(x= x_position_number,y=y_position_number)
        x_position_number =40
        y_position_number += 50


#
#       INSERT BUTTON OPERATION
#
Button(root,height=1,width=1, text="=",command=btn_equals_input).place(x= 218,y=310)
Button(root,height=1,width=1, text = "C", command=btn_clear_display).place(x = 40, y = 65)
Button(root,height=1,width=1, text = "<--", command=btn_erase).place(x = 129, y = 65) 



ttk.Separator(root, orient='vertical').place(relx=0.47, rely=0, relwidth=0.2, relheight=1) 


#
#       SECTION RESULT
#

#   BINARIO, DECIMAL, HEXADECIMAL, OCTAL

Label(root, text="RESULTADOS").place(x=450,y=40)

Label(root, text="BINARIO").place(x=380,y=110)
var_binario = tk.StringVar()
tk.Label(root, bg = "white" ,textvariable = var_binario, width =15).place(x = 510, y = 110)


Label(root, text="DECIMAL").place(x=380,y=160)
var_decimal = tk.StringVar()
tk.Label(root, bg = "white" ,textvariable = var_decimal, width =15).place(x = 510, y = 160)


Label(root, text="HEXADECIMAL").place(x=380,y=210)
var_hexadecimal = tk.StringVar()
tk.Label(root, bg = "white" ,textvariable = var_hexadecimal, width =15).place(x = 510, y = 210)


Label(root, text="OCTAL").place(x=380,y=260)
var_octal = tk.StringVar()
tk.Label(root, bg = "white" ,textvariable = var_octal, width =15).place(x = 510, y = 260)

Button(root, text="CLEAR",command=btn_clear_all).place(x= 450,y=310)

root.mainloop() 
