from manager.player_manager import Player_manager
from manager.floor_manager import Floor_manager
from dungeon.display import Display
from dungeon.camera import Camera
from dungeon.floor import Floor
import pyxel


class Dungeon:
    def __init__(self, _id):
        self.__id: int = _id
        self.__name = 'ほげダンジョン'

        self.__FLOOR_NUMBERS: int = 5
        self.__floors: list[Floor] = self.generate_floors(self.__FLOOR_NUMBERS)

        self.__now_floor_index: int = -1
        self.__turn: int = 1

        self.__camera = Camera()

        # TODO: 0829 managers
        # character_manager
        # floor_manager
        self.__floor_manager: Floor_manager
        self.__player_manager: Player_manager


    @property
    def floors(self):
        pass

    @floors.getter
    def floors(self):
        return self.__floors

    # フロアをfloor_numbers階分生成する
    def generate_floors(self, floor_numbers):
        floors = []
        for i in range(floor_numbers):
            floors.append(Floor(_id=i))

        return floors

    # フロア到着時に一回だけ呼び出される
    def start_turn(self):
        # self.__now_floor = self.get_next_floor()
        self.__now_floor_index += 1

        # self.__floors[self.__now_floor_index].__spawn_player()
        # self.__floors[self.__now_floor_index].spawn_steps()
        # self.__floors[self.__now_floor_index].spawn_enemys()

        Display.show_number_of_floors(self.__now_floor_index+1)
        print('ターン:', self.__turn)
        self.__floor_manager = Floor_manager(self.__floors[self.__now_floor_index])
        self.__player_manager = Player_manager(self.__floor_manager.spawn_player())
        self.__floor_manager.set_layer_player(self.__player_manager.player)  # self.__floors[self.__now_floor_index].player_set_position()

    # ターンを進める
    def forward_turn(self):
        self.__camera.target = self.__floors[self.__now_floor_index].get_player_room_arounds()
        self.__camera.show()

        self.player_turn()

        """
        if (self.__floors[self.__now_floor_index].is_player_on_steps() == True):
            print('next')
            self.start_turn()

        self.__floors[self.__now_floor_index].enemy_set_position()
        """


    # 入力されたキーをチェックする
    # 現在は方向キーだけ実装済み
    def player_turn(self):
        # TODO: 0829 プレイヤーが動いた後に、エネミーが動くようにしたい。
        if pyxel.btnp(pyxel.KEY_D):
            self.__turn += 1
            print('ターン:', self.__turn)
            player_direction = 'right'
            # self.__floor_manager.is_can_move_character()
            want_to_move_position:list = self.__player_manager.get_want_to_move_room_address_and_position(player_direction)
            if (self.__floor_manager.is_can_move_neo(want_to_move_position[0], want_to_move_position[1])):
                self.__player_manager.set_position(room_address=want_to_move_position[0], position=want_to_move_position[1])
                self.__floor_manager.set_layer_player(self.__player_manager.player)
                # self.__player_manager.move_instruction(player_direction) #self.__floors[self.__now_floor_index].player_move(player_direction)
            self.__player_manager.print_status()
            # self.__floors[self.__now_floor_index].player_set_position()
            # self.__floors[self.__now_floor_index].enemy_move()

        elif pyxel.btnp(pyxel.KEY_A):
            self.__turn += 1
            print('ターン:', self.__turn)
            player_direction = 'left'
            self.__floors[self.__now_floor_index].player_move(player_direction)
            self.__floors[self.__now_floor_index].player_set_position()
            self.__floors[self.__now_floor_index].enemy_move()

        elif pyxel.btnp(pyxel.KEY_W):
            self.__turn += 1
            print('ターン:', self.__turn)
            player_direction = 'up'
            self.__floors[self.__now_floor_index].player_move(player_direction)
            self.__floors[self.__now_floor_index].player_set_position()
            self.__floors[self.__now_floor_index].enemy_move()

        elif pyxel.btnp(pyxel.KEY_S):
            self.__turn += 1
            print('ターン:', self.__turn)
            player_direction = 'down'
            self.__floors[self.__now_floor_index].player_move(player_direction)
            self.__floors[self.__now_floor_index].player_set_position()
            self.__floors[self.__now_floor_index].enemy_move()

        elif pyxel.btnp(pyxel.KEY_F):
            self.__floors[self.__now_floor_index].enemy_mind()

        elif pyxel.btnp(pyxel.KEY_E):
            self.__floors[self.__now_floor_index].player_attack()


    """
    TODO: 08/22 敵の命令を実装しないといけない
    1. ターゲット(プレイヤー)の座標を認識する
    2. ターゲットの座標と自分自身の座標を比べて
    3. 自分自身が進むべき方向を選定する

    * nマス以内にターゲットがいるときは、距離を詰める
    * プレイヤーの入力をチェックするみたいに実装したい
    * プレイヤーとエネミークラスの親クラスである、characterクラスに
        command抽象メソッドを実装して、それぞれのクラスで実装すればいいのでは？
        プレイヤークラスでは、キーボード入力をチェック
        エネミークラスでは、上のようにする
    """
    # def enemys_turn(self):
    #     self.__floors.enemy
    # def instruction_enemy(self):
