from shape import Shape

# LineクラスはShapeクラスの子クラス
class Line(Shape):
    def __init__(self, canvas, p1, p2, color='black'):
        # Shapeクラスの初期化メソッドを呼ぶ
        super().__init__("Line", canvas, color)
        self.start = p1
        self.end = p2

    def draw(self):
        self.canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, width=2.0, fill=self.color)