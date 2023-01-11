from tkinter import *

root = Tk()
root.title("경진 GUI")
root.geometry("640x480+300+300") # 가로*세로 + x좌표 + y좌표

Label(root, text="메뉴를 선택하세요", bg="yellow").pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다
btn_burger1 = Radiobutton(root, text="맥모닝", value=1, variable=burger_var)
btn_burger1.select() # 기본값 선택
btn_burger2 = Radiobutton(root, text="더블불고기버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="에그불고기버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요", bg="yellow").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select() # 기본값 선택
btn_drink2 = Radiobutton(root, text="제로콜라", value="제로콜라", variable=drink_var)
btn_drink3 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()