from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Item(Obj):
    def __init__(self, color):
        super().__init__(color, [-1, -1], [-1, -1])
        self.__name = 'アイテム'

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def create(self, x, y, u, v, size):
        w = size
        h = size

        if (size == 5):
            pyxel.blt(x*w, y*h, 0, u, v, 5, 5, 0)    # 5*5
        elif (size == 16):
            pyxel.blt(x*w, y*h, 0, u, v, 16, 16, 0)  # 16*16

    # def use(self):
    #     pass

    # def take_out(self):
    #     return self