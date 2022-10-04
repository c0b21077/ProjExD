import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)

def click_equal(event):
    eqn = entry.get()
    ans = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

def click_C(event):
    eqn = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0,eqn[:-1])

def click_AC(event):
    entry.delete(0,tk.END)

root = tk.Tk()
root.title("電卓")
root.geometry("380x560")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right")
entry.grid(row=0, column=0, columnspan=5)

r = 1
c = 0
numbers = list(range(9, -1, -1))
sign = ["/","*","-","+"] 

for i in numbers:
    button = tk.Button(root, text=f"{i}", font=("Times New Roman",30), width="4", height="2")
    button.bind("<1>", button_click)
    button.grid(row = r, column = c)
    c += 1
    if c == 3:
        c = 0
        r += 1

for i in sign:
    button = tk.Button(root, text=f"{i}", font=("Times New Roman",30), width="4", height="2")
    button.bind("<1>", button_click)
    button.grid(row = r, column = 4)
    r -= 1

button = tk.Button(root, text="C/AC", font=("Times New Roman",30), width="4", height="2")
button.bind("<1>", click_C)
button.bind("<3>", click_AC)
button.grid(row = 4, column = 1)

button = tk.Button(root, text="=", font=("Times New Roman",30), bg = "PowderBlue", width="4", height="2")
button.bind("<1>", click_equal)
button.grid(row = 4, column = 2)

root.mainloop()