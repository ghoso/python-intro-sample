class Shape():
    def __init__(self,name,canvas,color):
        self.name = name
        self.canvas = canvas
        self.color = color

    # ゲッターメソッド
    @property
    def foreground(self):
        print("Foreground color = ", self.color)
        return self.color

    # セッターメソッド
    @foreground.setter
    def foreground(self, new_color):
        print("Foreground Color = ", new_color)
        self.color = new_color

    def move(self, pos):
        None

    # スタティックメソッド
    @staticmethod
    def all_rights():
        print("All Rights Reserved by IT Akademeia")