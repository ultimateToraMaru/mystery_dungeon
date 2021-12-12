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

    @data.setter
    def data(self, data):
        self.__data = data

    # レイヤー上のオブジェクトに対してcreate指示を出すメソッド
    def draw(self, p_x, p_y, size=16):
        for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[r_x][r_y].create(r_x+p_x, r_y+p_y, size)

    # 対象オブジェクトをレイヤー上にセットするメソッド
    def set_position(self, object):
        self.__data[object.position[0]][object.position[1]] = object
        object.tmp_position = [object.position[0], object.position[1]]
        object.position = [object.position[0], object.position[1]]

    # レイヤー上を掃除するメソッド
    def clean(self):
        for p_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for p_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[p_x][p_y] = None_obj()

    def get_obj(self, x, y):
        obj = self.__data[x][y]
        self.__data[x][y] = None_obj()
        return obj
