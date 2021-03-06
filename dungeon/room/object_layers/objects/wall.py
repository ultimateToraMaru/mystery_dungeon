from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Wall(Obj):
    def __init__(self, color):
        super().__init__(color, [-1, -1], [-1, -1])

    def create(self, x, y, size):
        w = size
        h = size

        if (size == 5):
            pyxel.blt(x*w, y*h, img=0, u=16, v=16, w=5, h=5)    # 5*5
        elif (size == 16):
            pyxel.blt(x*w, y*h, img=0, u=16, v=16, w=16, h=16)  # 16*16
