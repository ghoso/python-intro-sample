from shape import Shape

class Square(Shape):
    count = 0
    def __init__(self, canvas, top_left, bottom_right, color='black'):
        super().__init__("Square", canvas, color)
        self.start = top_left
        self.end = bottom_right
        Square.count += 1

    def draw(self):
        self.canvas.create_rectangle(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color)

    # 追加メソッド
    def move(self, pos):
        self.canvas.create_rectangle(self.start.x, self.start.y, self.end.x, self.end.y, fill='white', outline='white')
        self.start.x = self.start.x + pos.x
        self.start.y = self.start.y + pos.y
        self.end.x = self.end.x + pos.x
        self.end.y = self.end.y + pos.y
        self.canvas.create_rectangle(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color)

    # クラスメソッド 
    @classmethod
    def print_num(cls):
        print("Square: ", cls.count, "objects.")