from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

def create_new_file():
    print("Creating new file")

menu = Menu(root)

# File Menu
menu_file = Menu(menu, tearoff = 0) # file tab in the menu(top taskbar)
menu_file.add_command(label="New File", command=create_new_file) # tab inside that shows up when File tab clicked
menu_file.add_command(label="New Window")
menu_file.add_separator()   # Thick line separating the above two and the the command below
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state ="disabled") # disables this command(cannot be clicked)
menu_file.add_command(label="Exit", command=root.quit)  # close this window when Exit command is clicked


menu.add_cascade(label="File", menu=menu_file) # the tab labeled "File", cascades down when clicked, showing the content added above

# Edit Menu(Empty value)
menu.add_cascade(label="Edit")

# Language Menu(choose one using radio button)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View Menu
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()