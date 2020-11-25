from tkinter import *

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# without set, even if you scroll down, the scrollbar goes back up
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1,32):
    listbox.insert(END, str(i) + "일")

listbox.pack(side="left")

scrollbar.config(command=listbox.yview)
# the scroll bar now can take care of the y-axis mvt of the listbox

root.mainloop()