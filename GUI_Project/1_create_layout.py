from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Image Combiner")

# File Button frame (Add, Delete)
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add = Button(file_frame, padx=5, pady=5, width=12, text="Add")
btn_add.pack(side="left", fill = "x", expand=True)

btn_delete = Button(file_frame, padx=5, pady=5, width=12, text="Delete")
btn_delete.pack(side="right", fill = "x", expand=True)

# List Frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx = 5, pady = 5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode = "extended", height = 15, yscrollcommand = scrollbar.set)
list_file.pack(side="left", fill = "both", expand=True)
scrollbar.config(command=list_file.yview)

# Save Path Frame
path_frame = LabelFrame(root, text="Saving Path")
path_frame.pack(fill="x", padx = 5, pady = 5, ipady = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx = 5, pady = 5)
# ipady == inner padding in y-axis

btn_dest_path = Button(path_frame, text = "Find", width = 10)
btn_dest_path.pack(side="right", padx = 5, pady = 5)

# Option Frame
frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx = 5, pady = 5, ipadx = 5, ipady = 5)

# Width
# Width Label
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx = 5, pady = 5)

# Width Combo
opt_width = ["Original", "1024", "800", "640"]

cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx = 5, pady = 5)

# Padding
# Padding Label
lbl_padding = Label(frame_option, text="Padding", width=8)
lbl_padding.pack(side="left", padx = 5, pady = 5)

# Padding Combo
opt_padding = ["None", "Narrow", "Medium", "Wide"]

cmb_padding = ttk.Combobox(frame_option, state="readonly", values=opt_padding, width=10)
cmb_padding.current(0)
cmb_padding.pack(side="left", padx = 5, pady = 5)

# Format
# Format Label
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx = 5, pady = 5)

# Format Combo
opt_format = ["PNG", "JPG", "BMP"]

cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx = 5, pady = 5)

# Progress Bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx = 5, pady = 5)

p_var = DoubleVar()

progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var)
progress_bar.pack(fill="x", padx = 5, pady = 5)

# Run Frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx = 5, pady = 5, ipadx = 5)

btn_close = Button(frame_run, padx=5, pady = 5, text = "Close", width = 12, command=root.quit)
btn_close.pack(side="right")

btn_run = Button(frame_run, padx = 5, pady = 5, text = "Run", width=12)
btn_run.pack(side="right")

root.resizable(False,False)
root.mainloop()