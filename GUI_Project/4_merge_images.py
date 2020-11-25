from tkinter import * # only imports whatever is stated in __all__
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk 
from tkinter import filedialog
from PIL import Image
import os

root = Tk()
root.title("Image Combiner")

# add selected files' paths
def add_file():
    files = filedialog.askopenfilenames(\
        title="Select image file.", \
            filetypes=(("PNG", "*.png"), ("All files","*.*")),\
            initialdir="D:/Python/Chess Project/images") # shows C:/ when the window opens
            # first part of the tuple is file type name(just what's gon be in the option to chooses)
            # second part shows the type of file names that will show up

    for file in files:
        list_file.insert(END, file)

# delete the file paths selected in the window
def del_file():
    # reversed selection to avoid skipping after deletion
    for index in reversed(list_file.curselection()): # current selection
        list_file.delete(index)

# browse destination path
# folder
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(END, folder_selected)

# merge selected images
def merge_image():
    # print(list_file.get(0,END))
    images = [Image.open(path) for path in list_file.get(0,END)]
    # size -> size[0] : width, size[1] : height
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]

    widths, heights = zip(*(x.size for x in images))
    
    max_width, total_height = max(widths), sum(heights)
    
    result_img = Image.new("RGB", (max_width, total_height),(255,255,255))
    y_offset = 0 # y position
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1]

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1) / len(images) * 100 # add 1 to index bc it starts from 0
        p_var.set(progress)
        progress_bar.update()
        

    dest_path = os.path.join(txt_dest_path.get(), "nado_photo.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("Notification", "The process is complete")

def start():
    width = cmb_width.get()
    padding = cmb_padding.get()
    _format = cmb_format.get()

    if list_file.size() == 0:
        msgbox.showwarning("Alert", "Add an image file")
        return
    merge_image()
    


# File Button frame (Add, Delete)
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add = Button(file_frame, padx=5, pady=5, width=12, text="Add", command=add_file)
btn_add.pack(side="left", fill = "x", expand=True)

btn_delete = Button(file_frame, padx=5, pady=5, width=12, text="Delete", command=del_file)
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

btn_dest_path = Button(path_frame, text = "Browse", width = 10, command = browse_dest_path)
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

btn_run = Button(frame_run, padx = 5, pady = 5, text = "Run", width=12, command=start)
btn_run.pack(side="right")

root.resizable(False,False)
root.mainloop()