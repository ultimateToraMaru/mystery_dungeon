from dungeon.const.color import Color
from dungeon.const.size import Size
import pyxel
from dungeon.room.object_layers.objects.obj import Obj

class Attack_effect(Obj):
    def __init__(self, room_address, position, isMove):
        super().__init__(Color.BLACK, room_address, position)
        self.__loop_index = 0 # 0~2の範囲で描画(create)されるたびに値が変わるindex. loop_animationで使用。


    def create(self, x, y):
        self.__loop_animation()
        print('effect')

        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT

        if (Size.MASS_HEIGHT == 16):
            if (self.__loop_index == 0):
                pyxel.blt(x*w, y*h, img=0, u=16, v=32, w=16, h=16, colkey=0)
            elif (self.__loop_index == 1):
                pyxel.blt(x*w, y*h, img=0, u=32, v=32, w=16, h=16, colkey=0)
            elif (self.__loop_index == 2):
                pyxel.blt(x*w, y*h, img=0, u=48, v=32, w=16, h=16, colkey=0)

    def __loop_animation(self):
        if (self.__loop_index < 2):
            self.__loop_index += 1
        else:
            self.__loop_index = 0