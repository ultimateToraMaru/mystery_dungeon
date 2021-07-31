from dungeon.const.color import Color
from dungeon.const.size import Size
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Steps(Obj):
    def __init__(self):
        super().__init__(Color.BLACK)
    
    def create(self, x, y):
        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT

        # if (Size.MASS_HEIGHT == 5):
        #     pyxel.blt(x*w, y*h, img=0, u=0, v=0, w=5, h=5)    # 5*5
        # elif (Size.MASS_HEIGHT == 10):
        #     pyxel.blt(x*w, y*h, img=0, u=8, v=0, w=10, h=10)  # 10*10
        if (Size.MASS_HEIGHT == 16):
            pyxel.blt(x*w, y*h, img=0, u=0, v=32, w=16, h=16)  # 16*16