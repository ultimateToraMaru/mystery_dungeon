from dungeon.const.color import Color
from dungeon.const.size import Size
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Attack_effect(Obj):
    def __init__(self, room_address, position, isMove):
        super().__init__(Color.BLACK, room_address, position)

        self.__loop_index = 0 # 0~2の範囲で描画(create)されるたびに値が変わるindex. loop_animationで使用。
        self.__is_loop = False

    def create(self, x, y, size):
        self.__loop_animation()
        # print('effect')

        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT

        if (size == 16):
            if (self.__loop_index == 0 or self.__loop_index == 3):
                pyxel.blt(x*w, y*h, 0, 16, 32, 16, 16, 0)
            elif (self.__loop_index == 1 or self.__loop_index == 4):
                pyxel.blt(x*w, y*h, 0, 32, 32, 16, 16, 0)
            elif (self.__loop_index == 2 or self.__loop_index == 5):
                pyxel.blt(x*w, y*h, 0, 48, 32, 16, 16, 0)

    def __loop_animation(self):
        if (self.__is_loop):
            if (self.__loop_index < 2):
                self.__loop_index += 1
            else:
                self.__loop_index = 0
        else:
            self.__loop_index += 1