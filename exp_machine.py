# 描画する部分を格納する配列を持つカメラ
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj
import time
import pyxel


class Exp_machine():
    def __init__(self):
        self.__eye_catching_count = 0
        self.__target_floor_index = -1
        self.__dungeon_name = ''

    def set_index(self, dungeon_name, floor_index):
        self.__eye_catching_count = 30
        self.__dungeon_name = dungeon_name
        self.__target_floor_index = floor_index

    def show(self):
        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)
        pyxel.text(x=Size.MASS_HEIGHT/2, y=0, s=self.__dungeon_name, col=Color.WHITE)
        pyxel.text(x=Size.MASS_HEIGHT/2, y=Size.MASS_WIDTH/2, s=str(self.__target_floor_index)+'F', col=Color.WHITE)

        self.__eye_catching_count = self.__eye_catching_count - 1
        # print('aa',self.__eye_catching_count)

    def is_show_floor_index(self):
        return 0 < self.__eye_catching_count