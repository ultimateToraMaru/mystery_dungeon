import random
from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.trap import Trap
import pyxel
from dungeon.room.object_layers.objects.obj import Obj
import time

class Trap_warp(Trap):
    def __init__(self, room_address, position):
        super().__init__(room_address, position)

    def activate(self):
        super().activate()

        # ランダムなワープする部屋を設定
        r_x = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)
        r_y = random.randint(0, Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1)

        # プレイヤーに位置を設定
        self.target.room_address = [r_x, r_y]
        self.target.position = [5, 5]

        self.display.set_screen_log([
            'ワープトラップが発動！',
            self.target.name+'はワープしてしまった！'
        ])
        self.is_activate = True

        time.sleep(1)
