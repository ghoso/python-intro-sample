import tkinter as tk
from time import sleep
from square import Square
from line import Line
from point import Point

def app_init():
    root = tk.Tk()
    root.geometry("500x500")
    canvas =  tk.Canvas(root, height=500, width=500)
    canvas.place(x=0, y=0)
    return root, canvas

# メイン
r,c = app_init()
s1 = Square(c, Point(c, 100,100), Point(c, 200, 200))
s1.draw()
s2 = Square(c, Point(c, 10,10), Point(c, 50, 50))
s2.draw()
l1 = Line(c, Point(c, 50, 50), Point(c, 300, 300), color='red')
l1.draw()
# クラスメソッドを呼ぶ
Square.print_num()
Line.print_num()
# 親クラスのスタティックメソッドを呼ぶ
Square.all_rights()
# Tkボタンとハンドラー
def gmove():
    # セッターメソッド
    s1.foreground = 'blue'
    # 追加メソッド呼び出し
    s1.move(Point(c,10, 10))
    l1.move(Point(c,10,10))
    print(s1.foreground)
btn = tk.Button(r, text="Move", command=gmove)
btn.pack()
r.mainloop()