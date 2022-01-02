from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.trap import Trap
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Trap_damage(Trap):
    def __init__(self, room_address, position):
        super().__init__(room_address, position)
        self.__damage = 100

    def activate(self):
        self.target.hp -= self.__damage
        self.display.set_screen_log([
            'ダメージトラップが発動！',
            self.target.name+'に'+str(self.__damage)+'のダメージ！'
        ])
        self.is_activate = True
