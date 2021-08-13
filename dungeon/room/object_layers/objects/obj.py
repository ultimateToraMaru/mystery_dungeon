from abc import ABCMeta
from dungeon.const.size import Size
import pyxel

class Obj (metaclass=ABCMeta):
    def __init__(self, color, room_address, position):
        self.__color = color
        self.__room_address = room_address
        self.__position = position

    # colorのプロパティ
    @property
    def color(self):
        pass

    @color.getter
    def color(self):
        return self.__color

    def create(self, x, y):
        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT
        pyxel.rect(x*w, y*h, w, h, self.__color)