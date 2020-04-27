# Shapeクラス (Pointクラス、Lineクラス、Squareクラスのスーパークラス)
class Shape():
    def __init__(self, name, canvas, color):
        self.name = name
        self.canvas = canvas
        self.color = color