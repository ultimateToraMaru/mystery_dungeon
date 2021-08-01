from dungeon.camera import Camera
from dungeon.floor import Floor
import pyxel


class Dungeon:
    def __init__(self):
        self.__floors = []

        self.__FLOOR_NUMBERS = 5
        for i in range(self.__FLOOR_NUMBERS):
            print(i)
            self.__floors.append(Floor())
        
        self.__name = 'ほげダンジョン'
        self.__now_stage: int = 0
        self.__turn: int = 1

        self.__now_floor = Floor()
        self.__camera = Camera()
    
    @property
    def floors(self):
        pass

    @floors.getter
    def floors(self):
        return self.__floors
    
    def start(self):
        self.__now_floor = self.get_next_floor()

        self.__now_floor.spawn_player()
        self.__now_floor.spawn_steps()

        print(self.__now_stage, '階')
    
    def turn_forward(self):
        self.__camera.target = self.__now_floor.get_player_room_arounds()
        self.__camera.show()

        self.input_check()

        if (self.__now_floor.is_player_on_steps() == True):
            print('next')
            self.start()

        self.__now_floor.player_set_position()
    
    def get_next_floor(self):
        self.__now_stage += 1
        next_floor = self.__floors[self.__now_stage-1]

        return next_floor
    
    def input_check(self):
        if pyxel.btnp(pyxel.KEY_D):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__now_floor.player_move('right')
        elif pyxel.btnp(pyxel.KEY_A):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__now_floor.player_move('left')
        elif pyxel.btnp(pyxel.KEY_W):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__now_floor.player_move('up')
        elif pyxel.btnp(pyxel.KEY_S):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__now_floor.player_move('down')
    