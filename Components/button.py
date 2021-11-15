from tkinter import *
from tkinter import ttk
#root = Tk()
#frm = ttk.Frame(root, padding=10)
#frm.grid()
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#root.mainloop()

class BUTTON():
    def __init__(self,value, onAction, width, height ):
        self.value = value
        self.onAction = onAction
        self.width = width
        self.height = height

        # _init_ create button
        (ttk.Button(text=self.value, command=self.onAction)).place(x=self.width,y=self.height)


