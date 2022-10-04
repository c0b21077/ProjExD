print("hello world")

import tkinter as tk

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

r = 0
c = 0

for i in range(9, -1, -1):
    button = tk.Button(root, text=f"{i}", font=("Times New Roman",30), width="4", height="2")
    button.grid(row = r, column = c)
    c += 1
    if c == 3:
        c = 0
        r += 1

root.mainloop()