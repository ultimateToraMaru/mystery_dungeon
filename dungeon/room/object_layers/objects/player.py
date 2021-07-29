from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.const.color import Color
from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel

class Player(Obj):
    def __init__(self, color):
        super().__init__(color)
        self.__position = [0, 0]
        # self.__map = 
    
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
        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT
        
        if (Size.MASS_HEIGHT == 5): 
            # pyxel.rect(x*w, y*h, w, h, Color.CLOUDBLUE)    # 仮の色を渡しておく
            pyxel.blt(x*w, y*h, img=1, u=0, v=0, w=5, h=5)    # 5*5
        elif (Size.MASS_HEIGHT == 10):
            pyxel.blt(x*w, y*h, img=1, u=8, v=0, w=10, h=10, colkey=0)    # 10*10
        elif (Size.MASS_HEIGHT == 16):
            pyxel.blt(x*w, y*h, img=1, u=0, v=16, w=16, h=16, colkey=0)    # 10*10
    
    def move(self, direction):
        # print('move')
        if (direction == 'right'):
            self.position[0] = self.position[0]+1

        elif (direction == 'left'):
            self.position[0] = self.position[0]-1

        elif (direction == 'up'):
            self.position[1] = self.position[1]-1

        elif (direction == 'down'):
            self.position[1] = self.position[1]+1
    
    # def is_can_move(self, direction):
    #     if (direction == 'right'):
    #         if (type(self.position[0]+1) == None_obj):
    #             return True
                