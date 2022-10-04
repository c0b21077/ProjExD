import tkinter as tk
import tkinter.messagebox as tkm

#数字や演算子を入力する関数
def button_click(event): 
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)

#計算結果を表示する関数
def click_equal(event): 
    eqn = entry.get()
    ans = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

#入力文字を一文字消す関数
def click_C(event): 
    eqn = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0,eqn[:-1])

#入力文字をすべて消す関数
def click_AC(event): 
    entry.delete(0,tk.END)

root = tk.Tk()
root.title("電卓")
root.geometry("380x560")

#入力する場所
entry = tk.Entry(root, width=10, font=(", 40"), justify="right")
entry.grid(row=0, column=0, columnspan=5)

row_num = 1
column_num = 0
numbers = list(range(9, -1, -1)) #数字のリスト
sign = ["/","*","-","+"]  #記号のリスト

#数字のボタン
for i in numbers:
    button = tk.Button(root, text=f"{i}", font=("Times New Roman",30), width="4", height="2")
    button.bind("<1>", button_click)
    button.grid(row = row_num, column = column_num)
    column_num += 1
    if column_num == 3:
        column_num = 0
        row_num += 1

#記号のボタン
for i in sign:
    button = tk.Button(root, text=f"{i}", font=("Times New Roman",30), width="4", height="2")
    button.bind("<1>", button_click)
    button.grid(row = 1, column = 4)
    row_num += 1

#クリア・オールクリアのボタン
button = tk.Button(root, text="C/AC", font=("Times New Roman",30), width="4", height="2")
button.bind("<1>", click_C)
button.bind("<3>", click_AC)
button.grid(row = 4, column = 1)

#イコール（＝）ボタン
button = tk.Button(root, text="=", font=("Times New Roman",30), bg = "PowderBlue", width="4", height="2")
button.bind("<1>", click_equal)
button.grid(row = 4, column = 2)

root.mainloop()