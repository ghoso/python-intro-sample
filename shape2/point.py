from shape import Shape

# PointクラスはShapeクラスの子クラス
class Point(Shape):
    def __init__(self, canvas, x, y, color='black'):
        # Shapeクラスの初期化メソッドを呼ぶ
        super().__init__("Point", canvas, color)
        self.x = x
        self.y = y

    def draw(self):
        None