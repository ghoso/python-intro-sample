from shape import Shape

class Line(Shape):
    count = 0
    def __init__(self, canvas, p1, p2, color = 'black'):
        super().__init__("Line",canvas, color)
        self.start = p1
        self.end = p2
        Line.count += 1

    def draw(self):
        self.canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, width=2.0, fill=self.color)

    # 追加メソッド 
    def move(self, pos):
        self.canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, width=2.0, fill='white')
        self.start.x = self.start.x + pos.x
        self.start.y = self.start.y + pos.y
        self.end.x = self.end.x + pos.x
        self.end.y = self.end.y + pos.y
        self.canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, width=2.0, fill=self.color)

    # クラスメソッド
    @classmethod
    def print_num(cls):
        print("Line: ", cls.count, "objects.")