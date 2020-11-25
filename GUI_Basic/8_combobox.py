from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

value = [str(i) + "일" for i in range(1,32)]
combobox= ttk.Combobox(root, height=5, values=value)
combobox.pack()
combobox.set("카드 결제일") # sets the first aka default element

# by setting the state="readonly", user cannot write into the combobox
ronly_combobox= ttk.Combobox(root, height=10, values=value, state="readonly")
ronly_combobox.current(0) # sets the default choice to be the first entry
ronly_combobox.pack()

# height decides the number of entries that will show up when clicked


def btncmd():
    print(combobox.get())
    print(ronly_combobox.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()