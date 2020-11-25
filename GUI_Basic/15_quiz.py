# QUIZ) Notepad using tkinter library

# [GUI Requirements]
# 1. Title : 제목 없음 - Windows Notepad
# 2. Menu : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
#     1) 열기 : mynote.txt 파일 내용 열어서 보여주기
#     2) 저장 : mynote.txt 파일에 현재 내용 저장하기
#     3) 끝내기 : 프로그램 종료
# 4. At start of the program, the body should be empty
# 5. status bar at the bottom not necessary
# 6. Window size and location should be adjustable
# 7. add a vertical scroll bar to the right 

import os
from tkinter import *
root = Tk()
root.title("제목 없음 - Windows Notepad")
root.geometry("640x480") # idk how to make it show up in the center of the screen

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill ="y")

txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(fill="both", expand=True)
# fill determines the direction the widget will expand(within however much space that is allocated for the widget)
# expand, when set to true, goes beyond however much that's been allocated and employs all available space within its parent window

current_path = os.path.dirname(__file__)
filename = os.path.join(current_path, "mynote.txt")

def openFile():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            root.title(file.name.split("\\")[-1])
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def saveFile():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))
        txt.delete("1.0", END)
    
# Big menu that will contain all other cascade menus
menu = Menu(root)

menu_file = Menu(menu, tearoff=0) # tearoff signifies whether you can pop this menu out or not
menu_file.add_command(label="Open", command = openFile)
menu_file.add_command(label="Save", command = saveFile)
menu_file.add_separator()
menu_file.add_command(label="Close", command = root.quit)

menu.add_cascade(label = "File", menu = menu_file)
menu.add_cascade(label = "Edit")
menu.add_cascade(label = "Format")
menu.add_cascade(label = "View")
menu.add_cascade(label = "Help")


# config
scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
