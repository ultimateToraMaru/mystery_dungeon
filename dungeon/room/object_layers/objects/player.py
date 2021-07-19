from dungeon.const.color import Color
from dungeon.const.properties import Properties
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Player(Obj):
    def __init__(self, color):
        super().__init__(color)
        self.__position = [0, 0]
    
    @property
    def position(self):
        pass

    @position.getter
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
    
    def create(self, x, y):
        w = Properties.MASS_WIDTH
        h = Properties.MASS_HEIGHT
        print('player', w, h)
        pyxel.rect(x*w, y*h, w, h, Color.CLOUDBLUE)    # 仮の色を渡しておく