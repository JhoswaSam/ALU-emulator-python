import tkinter as tk

from Components.button import BUTTON
from Funtions.funtion import *


root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")

boton = BUTTON("Hola Mundo !!", saludar , 50, 50) 

root.mainloop() 

