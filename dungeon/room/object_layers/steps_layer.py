from dungeon.room.object_layers.objects.none_obj import None_obj
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 階段を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Steps_layer():
    def __init__(self):
        self.__data = [[None_obj()] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]
        self.__steps_position = [0, 0]
    
    @property
    def data(self):
        pass

    @data.getter
    def data(self):
        return self.__data
    
    @property
    def steps_position(self):
        pass

    @steps_position.getter
    def steps_position(self):
        return self.__steps_position

    @steps_position.setter
    def steps_position(self, steps_position):
        self.__steps_position = steps_position
    
    def draw(self, room_x, room_y):
        # for文で__dataを回して、drawしていく
        # print(room_x, room_y)
        # print(self.__data[0][0])
        for x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[x][y].create(x+room_x, y+room_y)
    
    # @property
    # def steps(self):
    #     pass

    # @steps.setter
    # def data(self, steps):
    #     self.__steps = steps


    