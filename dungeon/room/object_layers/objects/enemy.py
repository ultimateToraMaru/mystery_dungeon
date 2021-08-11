from dungeon.display import Display
from dungeon.room.object_layers.objects.character import Character
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Enemy(Character):
    def __init__(self, color, room_address, position):
        super().__init__(color)
        self.room_address = room_address
        self.position = position
        # Display.show_status(self.level, self.hp, self.MAX_HP, self.mp, self.MAX_MP, self.attack, self.defense)
        # self.__target = target
    
    def create(self, x, y):
        super().create(x, y, u=16, v=64)
                