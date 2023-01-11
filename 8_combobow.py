import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("경진 GUI")
root.geometry("640x480+300+300") # 가로*세로 + x좌표 + y좌표

values = [str(i)+"일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.set("카드 결제일") # 최초 목록 제목
combobox.pack()

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값을 출력
    print(readonly_combobox.get())
btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()