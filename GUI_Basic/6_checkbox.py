from tkinter import *

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

chkvar = IntVar()
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)
chkbox.select() # check the checkbox
chkbox.deselect() # uncheck the checkbox
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: unchecked
                        # 1: checked
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()