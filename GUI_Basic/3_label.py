import os
from tkinter import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")

label1 = Label(root, text = "Hello")
label1.pack()

photo = PhotoImage(file=resource_path("gui_basic/image.png"))
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text="See you again")

    global photo2 # if not global the garbage collector will get rid of it after the function call
    photo2 = PhotoImage(file=resource_path("gui_basic/image2.png"))
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()