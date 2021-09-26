from manager.enemy_manager import Enemy_manager
from manager.player_manager import Player_manager
from manager.character_manager import Character_manager
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
        self.__enemy_manager_list: list[Enemy_manager] = []


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

        # manager
        self.__floor_manager = Floor_manager(self.__floors[self.__now_floor_index])
        self.__player_manager = Player_manager(self.__floor_manager.spawn_player())
        self.__floor_manager.set_layer_player(self.__player_manager.character)  # self.__floors[self.__now_floor_index].player_set_position()

        enemys = self.__floor_manager.spawn_enemys()
        for i, enemy in enumerate(enemys):
            enemys[i].target = self.__player_manager.character
            self.__enemy_manager_list.append(Enemy_manager(enemy))

        # self.__floor_manager.generate_enemy_layers(len(enemys))
        # print('enemylayers', len(self.__floor_manager.floor.rooms[0][0].layers.enemy_layers))

    # ターンを進める
    def forward_turn(self):

        if  (not pyxel.btnp(pyxel.KEY_SHIFT) and ( pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_W) or pyxel.btnp(pyxel.KEY_S)  or pyxel.btnp(pyxel.KEY_E))):
            # self.__floor_manager.clean_floor()
            # self.__clean_floor()
            self.player_turn()
            self.enemys_turn()
            self.__alive_check()

        if (self.__floor_manager.is_player_on_steps(self.__player_manager.character) == True):
            print('next')
            self.start_turn()


    def __alive_check(self):
        # playerが死んだら、マネージャーはお役御免
        if (self.__player_manager.character.alive == False):
            del self.__player_manager
            print('********** GAME OVER **********')
            return

        for i, enemy_manager in enumerate(self.__enemy_manager_list):
            # enemyが死んだら、マネージャーはお役御免
            if (enemy_manager.character.alive == False):
                del self.__enemy_manager_list[i]
                return

    def __clean_floor(self):
        if (self.__player_manager.character.action == 'move'):
            self.__floor_manager.clean_player_layer()

        for i, enemy_manager in enumerate(self.__enemy_manager_list):
            if (enemy_manager.character.action == 'move'):
                self.__floor_manager.clean_enemy_layer()

    # 入力されたキーをチェックする
    # 現在は方向キーだけ実装済み
    def player_turn(self):
        # TODO: 0829 プレイヤーが動いた後に、エネミーが動くようにしたい。

        # # playerが死んだら、マネージャーはお役御免
        # if (self.__player_manager.character.alive == False):
        #     del self.__player_manager
        #     print('********** GAME OVER **********')
        #     return

        self.__player_manager.get_input()
        player_want_to_move_position:list = self.__player_manager.get_want_to_move_room_address_and_position()
        if (self.__player_manager.character.action != 'none'):
            self.__turn += 1
            print('ターン:', self.__turn)

            if (self.__player_manager.character.action == 'attack'):
                self.__floor_manager.attack_enemy(player_want_to_move_position[0], player_want_to_move_position[1], self.__player_manager.character)

            elif (self.__floor_manager.is_can_move_neo(player_want_to_move_position[0], player_want_to_move_position[1])):
                self.__floor_manager.clean_player_layer()
                # self.__floor_manager.clean_floor()
                self.__player_manager.set_position(room_address=player_want_to_move_position[0], position=player_want_to_move_position[1])
                self.__floor_manager.set_layer_player(self.__player_manager.character)

        self.__player_manager.print_status()

    def enemys_turn(self):
        for index, enemy_manager in enumerate(self.__enemy_manager_list):

            # # enemyが死んだら、マネージャーはお役御免
            # if (enemy_manager.character.alive == False):
            #     del self.__enemy_manager_list[i]
            #     return

            enemy_want_to_move_position:list = enemy_manager.get_want_to_move_room_address_and_position()


            # 行き止まりに行こうとしたら、考えを改めてもらう(行き止まりじゃない選択肢が出るまでループ)
            # TODO: ここで無限ループが発生
            if (enemy_manager.character.action == 'attack'):
                self.__floor_manager.attack_player(enemy_want_to_move_position[0], enemy_want_to_move_position[1], enemy_manager.character)
                return

            for j in range(100):
                enemy_manager.get_input()
                enemy_want_to_move_position:list = enemy_manager.get_want_to_move_room_address_and_position()
                if (self.__floor_manager.is_can_move_neo(enemy_want_to_move_position[0], enemy_want_to_move_position[1])):
                    # if (enemy_manager.character.action == 'move'):
                    #     self.__floor_manager.clean_enemy_layer()
                    enemy_manager.set_position(room_address=enemy_want_to_move_position[0], position=enemy_want_to_move_position[1])
                    self.__floor_manager.set_layer_enemy(enemy_manager.character, index)
                    break

    def camera_show(self):
        self.__camera.target = self.__floor_manager.get_player_room_arounds(self.__player_manager.character)
        self.__camera.show()
