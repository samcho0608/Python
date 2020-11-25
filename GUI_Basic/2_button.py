from tkinter import *

root = Tk()
root.title("Sam GUI")

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button2222222222222") # pads around the text
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="Button44444444444444444") # width and height fixed
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5") # the text and background color
btn5.pack()

photo = PhotoImage(file="gui_basic/image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Button Action")

btn7 = Button(root, text="Action Button", command = btncmd)
btn7.pack()

root.mainloop()