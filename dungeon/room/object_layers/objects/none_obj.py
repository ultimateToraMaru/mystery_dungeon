from dungeon.const.properties import Properties
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class None_obj(Obj):
    def __init__(self, color):
        super().__init__(color)
    
    def create(self, x, y):
        pass