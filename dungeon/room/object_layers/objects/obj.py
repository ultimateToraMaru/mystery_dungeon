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
    
    @property
    def room_address(self):
        pass

    @room_address.getter
    def room_address(self):
        return self.__room_address

    @room_address.setter
    def room_address(self, room_address):
        self.__room_address = room_address
    
    @property
    def position(self):
        pass

    @position.getter
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def create(self, x, y):
        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT
        pyxel.rect(x*w, y*h, w, h, self.__color)