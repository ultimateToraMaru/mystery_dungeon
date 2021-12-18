from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj
import time
import pyxel


class Eye_catching():
    """
    アイキャッチ画面のクラス
    """
    def __init__(self):
        # アイキャッチ表示時間を表すフィールド。数が大きいほど長く表示される。ただし、1 != 1s。
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

        # テキストをセット
        pyxel.text(x=Size.MASS_HEIGHT*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE/2, y=Size.MASS_WIDTH*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-Size.MASS_WIDTH, s=self.__dungeon_name, col=Color.WHITE)
        pyxel.text(x=Size.MASS_HEIGHT*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE/2, y=Size.MASS_WIDTH*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE, s=str(self.__target_floor_index)+'F', col=Color.WHITE)

        self.__eye_catching_count = self.__eye_catching_count - 1
        # print('aa',self.__eye_catching_count)



    def is_show(self):
        return 0 < self.__eye_catching_count