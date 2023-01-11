from tkinter import*

root = Tk()
root.title("경진GUI")
root.geometry("640x480+300+300")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1) #relief 테두리
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="맥모닝").pack()
Button(frame_burger, text="더블불고기버거").pack()
Button(frame_burger, text="에그불고기버거").pack()  

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="커피").pack()
Button(frame_drink, text="제로콜라").pack()

root.mainloop()