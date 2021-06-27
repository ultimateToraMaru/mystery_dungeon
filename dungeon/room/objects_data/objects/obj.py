from abc import ABCMeta
import pyxel

class Obj (metaclass=ABCMeta):
    def __init__(self, color):
        self.__color = color
        self.__MASS_WIDTH = 5
        self.__MASS_HEIGHT = 5

    # colorのプロパティ
    @property
    def color(self):
        pass

    @color.getter
    def color(self):
        return self.__color

    def create(self, x, y):
        w = self.__MASS_WIDTH
        h = self.__MASS_HEIGHT

        pyxel.rect(x*w, y*h, w, h, self.__color)