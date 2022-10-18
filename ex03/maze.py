import tkinter as tk
import tkinter.messagebox as tkm
from random import randint

#練習8
import maze_maker as mm

#練習5
def key_down(event):
    global key
    key = event.keysym

#練習6
def key_up(event):
    global key
    key = ""

#練習7,11
def main_proc():
    global mx, my
    global cx, cy

    #経過時間
    global tmr
    tmr += 1

    #穴の追加
    n = randint(0,14)
    m = randint(0, 8)

    if mx == n and my == m:
        tkm.showinfo("穴","ゲームオーバー")
        mx, my = 1, 1
    
    if mx == 13 and my == 7:
        tkm.showinfo("迷路",f"おめでとう！！！\n{tmr/10}秒かかった！")
        mx, my = 1, 1

    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1
    
    #練習12
    if maze_lst[my][mx] == 0: #床
        cx, cy = mx * 100 + 50, my * 100 + 50
    else: #壁
        if key == "Up":
            my += 1
        elif key == "Down":
            my -= 1
        elif key == "Left":
            mx += 1
        elif key == "Right":
            mx -= 1
    
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    tmr = 0

    #練習1,2
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canv.pack()

    #練習9,10
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv, maze_lst)

    #スタート、ゴールの追加
    start = tk.PhotoImage(file = "fig/start.png")
    goal = tk.PhotoImage(file = "fig/goal.png")
    canv.create_image(150,150, image = start)
    canv.create_image(1350,750, image = goal)

    #練習3
    tori = tk.PhotoImage(file = "fig/8.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canv.create_image(cx, cy, image = tori, tag = "tori")

    #練習4,5,6,7
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()