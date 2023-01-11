from tkinter import *

root = Tk()
root.title("경진 GUI")

root.geometry("640x480+300+300") # 가로*세로 + x좌표 + y좌표

label1 = Label(root, text="내 이름은 김경진")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="반갑다.")
    global photo2
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()