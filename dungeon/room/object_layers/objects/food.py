from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.item import Item
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Food(Item):
    def __init__(self, color=Color.WHITE):
        super().__init__(color)
        self.name = 'フード'

    def eat(self):
        pass