from dungeon.display import Display
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
        self.__now_floor_index: int = -1
        self.__turn: int = 1

        # self.__now_floor = Floor()      # いらない。now_floor_indexがあれば、この変数はいらない。いつか変えよう。
        self.__camera = Camera()
    
    @property
    def floors(self):
        pass

    @floors.getter
    def floors(self):
        return self.__floors
    
    # フロア到着時に一回だけ呼び出される
    def start_turn(self):
        # self.__now_floor = self.get_next_floor()
        self.__now_floor_index += 1

        self.__floors[self.__now_floor_index].spawn_player()
        self.__floors[self.__now_floor_index].spawn_steps()
        self.__floors[self.__now_floor_index].spawn_enemys()

        Display.show_number_of_floors(self.__now_floor_index+1)
    
    # ターンを進める
    def forward_turn(self):
        self.__camera.target = self.__floors[self.__now_floor_index].get_player_room_arounds()
        self.__camera.show()

        self.input_check()

        if (self.__floors[self.__now_floor_index].is_player_on_steps() == True):
            print('next')
            self.start_turn()

        self.__floors[self.__now_floor_index].player_set_position()
    

    # def get_next_floor(self):
    #     self.__now_floor_index += 1
    #     next_floor = self.__floors[self.__now_floor_index-1]

    #     return next_floor
    
    # 入力されたキーをチェックする
    # 現在は方向キーだけ実装済み
    def input_check(self):
        if pyxel.btnp(pyxel.KEY_D):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__floors[self.__now_floor_index].player_move('right')
        elif pyxel.btnp(pyxel.KEY_A):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__floors[self.__now_floor_index].player_move('left')
        elif pyxel.btnp(pyxel.KEY_W):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__floors[self.__now_floor_index].player_move('up')
        elif pyxel.btnp(pyxel.KEY_S):
            self.__turn += 1
            print('ターン:', self.__turn)
            self.__floors[self.__now_floor_index].player_move('down')
    