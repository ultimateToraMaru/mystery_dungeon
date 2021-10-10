from abc import ABCMeta
from dungeon.room.object_layers.objects.none_obj import None_obj
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# TODO: layerクラスの抽象クラス。
class Empty_layer(metaclass=ABCMeta):
    def __init__(self):
        self.__data = [[None_obj()] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]

    @property
    def data(self):
        pass

    @data.getter
    def data(self):
        return self.__data

    def draw(self, p_x, p_y):
        for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[r_x][r_y].create(r_x+p_x, r_y+p_y)
