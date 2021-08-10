from dungeon.const.size import Size
from dungeon.room.object_layers.objects.obj import Obj
import pyxel


class Character(Obj):
    def __init__(self, color):
        super().__init__(color)
        self.__room_address = [0, 0]
        self.__position = [0, 0]
        self.__direction = 'down'

        # ステータス
        self.__level = 1
        self.__hp: int = 100
        self.__MAX_HP: int = self.__hp
        self.__mp: int = 100
        self.__MAX_MP: int = self.__mp
        self.__attack: int = 100
        self.__defense: int = 100


    @property
    def room_address(self):
        pass

    @room_address.getter
    def room_address(self):
        return self.__room_address

    @room_address.setter
    def room_address(self, room_address):
        self.__room_address = room_address
    
    @property
    def position(self):
        pass

    @position.getter
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
    
    @property
    def direction(self):
        pass

    @direction.getter
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def level(self):
        pass

    @level.getter
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def hp(self):
        pass

    @hp.getter
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp
    
    @property
    def MAX_HP(self):
        pass

    @MAX_HP.getter
    def MAX_HP(self):
        return self.__MAX_HP

    @MAX_HP.setter
    def MAX_HP(self, MAX_HP):
        self.__MAX_HP = MAX_HP
    
    @property
    def mp(self):
        pass

    @mp.getter
    def mp(self):
        return self.__mp

    @mp.setter
    def hp(self, mp):
        self.__mp = mp

    @property
    def MAX_MP(self):
        pass

    @MAX_MP.getter
    def MAX_MP(self):
        return self.__MAX_MP

    @MAX_MP.setter
    def MAX_MP(self, MAX_MP):
        self.__MAX_MP = MAX_MP

    @property
    def attack(self):
        pass

    @attack.getter
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def defense(self):
        pass

    @defense.getter
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense
    
    def create(self, x, y, u, v):
        w = Size.MASS_WIDTH
        h = Size.MASS_HEIGHT
        
        if (Size.MASS_HEIGHT == 5): 
            # pyxel.rect(x*w, y*h, w, h, Color.CLOUDBLUE)    # 仮の色を渡しておく
            pyxel.blt(x*w, y*h, img=1, u=0, v=0, w=5, h=5)    # 5*5
        elif (Size.MASS_HEIGHT == 10):
            pyxel.blt(x*w, y*h, img=1, u=8, v=0, w=10, h=10, colkey=0)    # 10*10
        elif (Size.MASS_HEIGHT == 16):
            if (self.__direction == 'right'):
                pyxel.blt(x*w, y*h, img=1, u=u, v=v, w=16, h=16, colkey=0)    # 10*10
            elif (self.__direction == 'left'):
                pyxel.blt(x*w, y*h, img=1, u=u-32, v=v, w=16, h=16, colkey=0)    # 10*10
            elif (self.__direction == 'up'):
                pyxel.blt(x*w, y*h, img=1, u=u/2, v=v/2, w=16, h=16, colkey=0)    # 10*10
            elif (self.__direction == 'down'):
                pyxel.blt(x*w, y*h, img=1, u=u/2, v=v, w=16, h=16, colkey=0)    # 10*10
    
    def move(self, direction):
        # # print('move')
        self.__direction = direction
        if (direction == 'right'):
            self.position[0] = self.position[0]+1

        elif (direction == 'left'):
            self.position[0] = self.position[0]-1

        elif (direction == 'up'):
            self.position[1] = self.position[1]-1

        elif (direction == 'down'):
            self.position[1] = self.position[1]+1