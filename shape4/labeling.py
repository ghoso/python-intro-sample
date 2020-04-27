# Labelingクラス
#    描画オブジェクトに名前を表示
class Labeling:
    def __init__(self, label, pos):
        self.label = label
        self.x = pos.x
        self.y = pos.y

    def show(self, canvas, offset_x, offset_y):
        canvas.create_text(self.x + offset_x, self.y + offset_y, text=self.label)

    def move(self, canvas, new_pos):
        canvas.create_text(self.x, self.y, text=self.label, fill="white")
        self.x = new_pos.x
        self.y = new_pos.y
        canvas.create_text(self.x, self.y, text=self.label)