from tkinter import*
import os
root = Tk()
root.title("제목없음 - window 메모장")
root.geometry("640x480+300+100")

frame = Frame(root)
frame.pack()

def file_open():
    if os.path.isfile("mynote.txt"): #파일 있으면 True 없으면 False
        global mynote_file
        mynote_file = open("mynote.txt", "r", encoding="UTF8")
        lines = mynote_file.readlines()
        text.delete("1.0", END)
        for line in lines:
            text.insert(END, line)   
        mynote_file.close()

def file_save():
    global mynote_file
    mynote_file= open("mynote.txt", "w", encoding="UTF8")
    mynote_file.write(text.get("1.0", END))    
    mynote_file.close()

def file_delete():
    text.delete("1.0", END)

# 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기(open)", command=file_open)
menu_file.add_separator()
menu_file.add_command(label="저장(save)", command=file_save)
menu_file.add_separator()
menu_file.add_command(label="끝내기(exit)", command=root.quit)
menu_file.add_separator()

menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="삭제", command=file_delete)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

#scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
#scrollbar = Scrollbar(root)
#scrollbar.pack(side="right", fill="y")


#Text
text = Text(frame, width=640, height=480, yscrollcommand=scrollbar.set, font=6)
#text = Text(root, yscrollcommand=scrollbar.set )
#text.pack(side="left", fill="both", expand=True)
text.pack(side="left")

scrollbar.config(command=text.yview)

root.config(menu=menu)
root.mainloop()