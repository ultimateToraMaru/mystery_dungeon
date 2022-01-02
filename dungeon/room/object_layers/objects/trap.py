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
        self.__is_activate = False

    @property
    def target(self):
        pass

    @target.getter
    def target(self):
        return self.__target

    @target.setter
    def target(self, target):
        self.__target = target

    @property
    def display(self):
        pass

    @display.getter
    def display(self):
        return self.__display

    @display.setter
    def display(self, display):
        self.__display = display

    @property
    def is_activate(self):
        pass

    @is_activate.getter
    def is_activate(self):
        return self.__is_activate

    @is_activate.setter
    def is_activate(self, is_activate):
        self.__is_activate = is_activate

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

        return  (self.room_address == self.__target.room_address
            and self.position == self.__target.position)


    def activate(self):
        pass