import pyxel

class Tile(object):
    def __init__(self, color) :
        super().__init__()
        self.__color = color

    # colorのプロパティ
    @property
    def color(self):
        pass

    @color.getter
    def color(self):
        return self.__color

    def create(self, x, y):
        w=1
        h=1
        pyxel.rect(x, y, w, h, self.__color)