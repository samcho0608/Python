from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

# when we don't know when something will end
# progressbar = ttk.Progressbar(root, maximum = 100, mode="indeterminate")

# progressbar = ttk.Progressbar(root, maximum = 100, mode="determinate")

# progressbar.start(10) # moves every 10 ms
# progressbar.pack()



# def btncmd():
#     progressbar.stop()  # stops the progress
#                         # this STOPs not RESUMES

# btn = Button(root, text="stop", command=btncmd)
# btn.pack()


p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # sets the value of progress bar
        progressbar2.update() # update the ui(to illustrate the gradual change)
        print(p_var2.get())


btn = Button(root, text="start", command=btncmd2)
btn.pack()


root.mainloop()