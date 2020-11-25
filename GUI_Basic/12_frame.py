from tkinter import *

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

Label(root, text="Select your menu").pack(side="top")

Button(root, text="Make your order").pack(side="bottom")


frame_burger = Frame(root, relief="solid", bd=1)
# relief signiifies boundary shape
# bd means the thickness of the external boundary(?)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Chicken burger").pack()
Button(frame_burger, text="Cheese burger").pack()

frame_drink = LabelFrame(root, text="Drinks")
frame_drink.pack(side="right", fill = "both", expand =True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()


root.mainloop()