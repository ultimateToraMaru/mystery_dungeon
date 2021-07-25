from dungeon.const.properties import Properties
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Tile(Obj):
    def __init__(self, color):
        super().__init__(color)
    
    def create(self, x, y):
        w = Properties.MASS_WIDTH
        h = Properties.MASS_HEIGHT

        pyxel.blt(x*w, y*h, img=0, u=0, v=0, w=5, h=5)