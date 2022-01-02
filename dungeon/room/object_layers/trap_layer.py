from abc import ABCMeta
from dungeon.room.object_layers.empty_layer import Empty_layer
from dungeon.room.object_layers.objects.none_obj import None_obj
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.trap import Trap
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# TODO: layerクラスの抽象クラス。
class Trap_layer(Empty_layer):
    def __init__(self):
        super().__init__()

    # レイヤー上のオブジェクトに対してcreate指示を出すメソッド
    def draw(self, p_x, p_y, size=16):
        for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                emp_obj = self.data[r_x][r_y]
                if (isinstance(emp_obj, Trap) and emp_obj.is_activate):
                    self.data[r_x][r_y].create(r_x+p_x, r_y+p_y, size)
