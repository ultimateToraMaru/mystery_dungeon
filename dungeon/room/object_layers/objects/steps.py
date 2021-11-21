from dungeon.const.color import Color
from dungeon.const.size import Size
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Steps(Obj):
    def __init__(self, room_address, position):
        super().__init__(Color.BLACK, room_address, position)

    def create(self, x, y, size):
        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT

        if (size == 5):
            pyxel.blt(x*w, y*h, img=1, u=0, v=32, w=5, h=5)    # 5*5

        if (size == 16):
            pyxel.blt(x*w, y*h, img=0, u=0, v=32, w=16, h=16)  # 16*16