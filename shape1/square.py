# 四角形クラス
class Square:
    # 初期化
    def __init__(self, canvas, top_left,bottom_right):
        self.start = top_left
        self.end = bottom_right
        self.canvas = canvas

    # 描画メソッド
    def draw(self):
        self.canvas.create_rectangle(self.start.x, self.start.y, self.end.x, self.end.y, fill='black')