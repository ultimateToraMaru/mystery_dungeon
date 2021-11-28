from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Item(Obj):
    def __init__(self, color):
        super().__init__(color, [-1, -1], [-1, -1])

    def create(self, x, y, u, v, size):
        w = size
        h = size

        if (size == 5):
            pyxel.blt(x*w, y*h, img=0, u=u, v=v, w=5, h=5, colkey=0)    # 5*5
        elif (size == 16):
            pyxel.blt(x*w, y*h, img=0, u=u, v=v, w=16, h=16, colkey=0)  # 16*16

    def use(self):
        pass