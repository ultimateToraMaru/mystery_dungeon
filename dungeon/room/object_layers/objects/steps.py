from dungeon.const.color import Color
from dungeon.const.size import Size
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Steps(Obj):
    def __init__(self, room_address, position):
        super().__init__(Color.BLACK, room_address, position)

    def create(self, x, y, size):
        w = size
        h = size

        if (size == 5):
            pyxel.blt(x*w, y*h, img=1, u=0, v=5, w=5, h=5, colkey=0)    # 5*5

        if (size == 16):
            pyxel.blt(x*w, y*h, img=0, u=0, v=32, w=16, h=16, colkey=0)  # 16*16