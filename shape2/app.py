import tkinter as tk
from square import Square
from line import Line
from point import Point

# 初期化
def app_init():
    root = tk.Tk()
    root.geometry("500x500")
    canvas = tk.Canvas(root, height=500, width=500)
    canvas.place(x=0, y=0)
    return root, canvas

# メイン
r,c = app_init()
s1 = Square(c, Point(c, 100,100), Point(c, 200, 200), 'black')
s1.draw()
l1 = Line(c, Point(c, 50, 50), Point(c, 300, 300), 'red')
l1.draw()
r.mainloop()