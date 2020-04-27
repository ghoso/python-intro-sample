from shape import Shape
from labeling import Labeling

class Line(Shape):
    def __init__(self, canvas, name, p1, p2, color='black'):
        super().__init__(name, canvas, color)
        self.start = p1
        self.end = p2
        # Labelingクラス集約（コンポジション）
        self.labeling = Labeling(self.name, self.start)

    def draw(self):
        self.canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, width=2.0, fill=self.color)
        # Labelingクラスのメソッドを呼ぶ
        self.labeling.show(self.canvas, 20, 0)