from dungeon.const.color import Color
from dungeon.const.size import Size
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Tile(Obj):
    def __init__(self):
        super().__init__(Color.BLACK, [-1, -1], [-1, -1])

    def create(self, x, y, size):
        w = size
        h = size

        if (size == 5):
            pyxel.blt(x*w, y*h, img=0, u=0, v=16, w=5, h=5)    # 5*5
        # elif (Size.MASS_HEIGHT == 10):
        #     pyxel.blt(x*w, y*h, img=0, u=8, v=0, w=10, h=10)  # 10*10
        elif (size == 16):
            pyxel.blt(x*w, y*h, img=0, u=0, v=16, w=16, h=16)  # 16*16