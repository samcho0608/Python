from tkinter import *

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Enter a word: ")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Enter one line only: ")

def btncmd():
    print(txt.get("1.0", END))
    # 1 signifies first line
    # 0 signifies index 0
    # END signifies to the end
    print(e.get()) # the same as above but for entry

    # delete content
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()