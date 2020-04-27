# モジュールインポート
import tkinter as tk
from square import Square
from line import Line
from point import Point

# 初期化
def app_init():
    root = tk.Tk()
    root.geometry("500x500")
    canvas =  tk.Canvas(root, height=500, width=500)
    canvas.place(x=0, y=0)
    return root, canvas

# メイン
r,c = app_init()
# 四角形オブジェクト生成
s1 = Square(c, Point(100,100), Point(200,200))
# draw()メソッド呼び出し
s1.draw()
# 直線オブジェクト生成
l1 = Line(c, Point(50,50), Point(300, 300))
#  draw()メソッド呼び出し
l1.draw()
# Tkinterメインループ
r.mainloop()