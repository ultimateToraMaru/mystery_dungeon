from abc import ABCMeta
from dungeon.const.properties import Properties
import pyxel

class Obj (metaclass=ABCMeta):
    def __init__(self, color):
        self.__color = color

    # colorのプロパティ
    @property
    def color(self):
        pass

    @color.getter
    def color(self):
        return self.__color

    def create(self, x, y):
        w = Properties.MASS_WIDTH
        h = Properties.MASS_HEIGHT
        pyxel.rect(x*w, y*h, w, h, self.__color)