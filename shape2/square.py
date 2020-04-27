from shape import Shape

# SquareクラスはShapeクラスの子クラス
class Square(Shape):
    def __init__(self, canvas, top_left, bottom_right, color='black'):
        # Shapeクラスの初期化メソッドを呼ぶ
        super().__init__("Square", canvas, color)
        self.start = top_left
        self.end = bottom_right

    def draw(self):
        self.canvas.create_rectangle(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color)