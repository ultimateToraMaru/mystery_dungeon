from dungeon.room.object_layers.objects.none_obj import None_obj
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# エフェクトを表すクラス。地形データ__dataにAttack_effect()などが入る
class Effect_layer():
    def __init__(self):
        self.__data = [[None_obj()] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]

    @property
    def data(self):
        pass

    @data.getter
    def data(self):
        return self.__data

    def set_position(self, effect):
        self.__data[effect.position[0]][effect.position[1]] = effect
        effect.tmp_position = [effect.position[0], effect.position[1]]
        effect.position = [effect.position[0], effect.position[1]]

    def clean(self):
        for p_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for p_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[p_x][p_y] = None_obj()

    def draw(self, p_x, p_y):
        for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[r_x][r_y].create(r_x+p_x, r_y+p_y, size=16)
