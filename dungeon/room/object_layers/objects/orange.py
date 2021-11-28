from dungeon.const.size import Size
from dungeon.room.object_layers.objects.item import Item
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Orange(Item):
    def __init__(self, color):
        super().__init__(color)

    def create(self, x, y, size):
        w = size
        h = size

        if (size == 5):
            super().create(x, y, 16, 10, size)
        elif (size == 16):
            super().create(x, y, 16, 0, size)