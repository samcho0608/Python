from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Sam GUI")
root.geometry("640x480")    # width x height

def info():
    msgbox.showinfo("Notification", "Successfully ticketed")
    #                   title           content

def warn():
    msgbox.showwarning("Alert", "The selected seat cannot be purchased")

def error():
    msgbox.showerror("Error", "Error occurred while purchasing")

def okcancel():
    msgbox.askokcancel("Confirm / Cancel", "The selected seat is for the disabled, Would you like to continue purchasing?")

def retrycancel():
    msgbox.askretrycancel("Retry / Cancel", "Temporary Error, would you like to retry purchasing?")
    # when only two choice give, first is 1, second is 0

def yesno():
    msgbox.askyesno("Yes / No", "The selected seat looks at the opposite direction, would you like to retry purchasing?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Ticketing History not saved.\n Would you like to save and close?")
    # yes : save and close
    # no : close without saving
    # cancel : cancel closing program
    print("response: ", response) # True, False, None -> yes 1, no 0, otherwise
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")

Button(root, command=info, text="Notification").pack()
Button(root, command=warn, text="Alert").pack()
Button(root, command=error, text="Error").pack()

Button(root, command=okcancel, text="Confirm / Cancel").pack()
Button(root, command=retrycancel, text="Retry / Cancel").pack()
Button(root, command=yesno, text= "yes or no").pack()
Button(root, command=yesnocancel, text= "yes no cancel").pack()


root.mainloop()