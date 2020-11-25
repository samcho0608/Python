from tkinter import *

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

listbox = Listbox(root, selectmode = "extended", height=0)
# extended: can select multiple
# single: can only select one
# height: how many options to show(0 shows all elements)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grapes")
listbox.pack()

def btncmd():
    # delete from bottom
    # listbox.delete(END)
    
    # delete from top
    # listbox.delete(0)

    # print count of entries
    # print("count: ", listbox.size())

    # getter
    # print("First to third entries: ", listbox.get(0,2))
    # lower and upper bound both inclusive

    # selected entry
    print("Currently selected: ", listbox.curselection())
    # returns the index of the currently selected entries

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()