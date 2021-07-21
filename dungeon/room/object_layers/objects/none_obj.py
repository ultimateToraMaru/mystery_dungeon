from dungeon.const.color import Color
from dungeon.const.properties import Properties
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class None_obj(Obj):
    def __init__(self):
        super().__init__(Color.BLACK)
    
    def create(self, x, y):
        pass