from dungeon.display import Display
from dungeon.room.object_layers.objects.character import Character
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Enemy(Character):
    def __init__(self, color):
        super().__init__(color)
        # Display.show_status(self.level, self.hp, self.MAX_HP, self.mp, self.MAX_MP, self.attack, self.defense)
        # self.__target = target
    
    def create(self, x, y):
        super().create(x, y, u=32, v=32)
                