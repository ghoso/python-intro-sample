# 直線クラス
class Line:
    # 初期化
    def __init__(self, canvas, p1, p2):
        self.canvas = canvas
        self.start = p1
        self.end = p2
    # 描画メソッド
    def draw(self):
        self.canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, width=2.0, fill='red')