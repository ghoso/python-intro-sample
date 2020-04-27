from shape import Shape
from labeling import Labeling

class Square(Shape):
    def __init__(self, canvas, name, top_left, bottom_right, color='black'):
        super().__init__(name, canvas, color)
        self.start = top_left
        self.end = bottom_right
        # Labelingクラス集約（コンポジション）
        self.labeling = Labeling(name, self.start)

    def draw(self):
        self.canvas.create_rectangle(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color)
        # Labelingクラスのメソッドを呼ぶ
        self.labeling.show(self.canvas, 20, -10)