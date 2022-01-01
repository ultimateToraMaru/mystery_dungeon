from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.character import Character
from dungeon.room.object_layers.objects.none_obj import None_obj
import pyxel
from dungeon.room.object_layers.objects.obj import Obj
from tools.display import Display

class Trap(Obj):
    def __init__(self, room_address, position):
        super().__init__(Color.BLACK, room_address, position)
        self.__target: Character = None_obj()
        self.__display: Display = Display.get_instance()

    @property
    def target(self):
        pass

    @target.getter
    def target(self):
        return self.__target

    @target.setter
    def target(self, target):
        self.__target = target

    def create(self, x, y, size):
        w = size
        h = size

        if (size == 5):
            pyxel.blt(x*w, y*h, 1, 0, 5, 5, 5, 0)    # 5*5

        if (size == 16):
            pyxel.blt(x*w, y*h, 0, 32, 16, 16, 16, 0)  # 16*16

    def check_target(self):
        """
        ターゲット(プレイヤー)の位置と自分の位置をチェックして、<br>
        同じだった場合、トラップを発動する
        """

        if (self.room_address == self.__target.room_address
            and self.position == self.__target.position):

            print('発動！')
            self.__activate()

        else :
            # print('何も起こらない')
            pass


    def __activate(self):
        pass