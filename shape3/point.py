from shape import Shape

class Point(Shape):
    def __init__(self, canvas, x, y, color='black'):
        super().__init__("Point", canvas, color)
        self.x = x
        self.y = y