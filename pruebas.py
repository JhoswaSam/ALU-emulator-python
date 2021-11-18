from tkinter import *

def retrieve_input():
    inputValue=text.get("1.0","end-1c")
    print(inputValue)

def insert_value(a):
    print(a)
    text.insert(INSERT,a)


class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)


    

root = Tk()
root.config(width=330, height=380)
root.title("ALU emulator")


text = Text(root, height=2, width=40)
text.pack()

buttonCommit=Button(root, height=1, width=10, text="Commit", command=lambda: retrieve_input())
buttonCommit.pack()


buttons = [1, 2, 3,4,4]
for i, b in enumerate(buttons):
    print(i,b)
    buttonInsert= Button(root,height=1,width=1,text=b, command=Callback(insert_value, b))
    buttonInsert.pack()


root.mainloop()