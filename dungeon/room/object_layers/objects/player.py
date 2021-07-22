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
        # pyxel.rect(x*w, y*h, w, h, Color.CLOUDBLUE)    # 仮の色を渡しておく
        pyxel.blt(x*w, y*h, img=1, u=0, v=0, w=4, h=4)
    
    def move(self, direction):
        if (direction == 'right'):
            self.position[0] = self.position[0]+1
            self.position[1] = self.position[1]