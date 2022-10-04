import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"「{num}のボタンがクリックされました」")
    entry.insert(tk.END, num)

def click_equal(event):
    eqn = entry.get()
    ans = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

root = tk.Tk()
root.title("電卓")
root.geometry("300x600")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right")
entry.grid(row=0, column=0, columnspan=3)

r = 1
c = 0
numbers = list(range(9, -1, -1))
plus = ["+"]

for i in numbers + plus:
    button = tk.Button(root, text=f"{i}", font=("Times New Roman",30), width="4", height="2")
    button.bind("<1>", button_click)
    button.grid(row = r, column = c)
    c += 1
    if c == 3:
        c = 0
        r += 1

button = tk.Button(root, text="=", font=("Times New Roman",30), width="4", height="2")
button.bind("<1>", click_equal)
button.grid(row = r, column = c)

root.mainloop()