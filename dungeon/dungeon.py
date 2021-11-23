from manager.enemy_manager import Enemy_manager
from manager.player_manager import Player_manager
from manager.character_manager import Character_manager
from manager.floor_manager import Floor_manager
from dungeon.display import Display
from dungeon.camera import Camera
from dungeon.floor import Floor
import pyxel
import time


class Dungeon:
    def __init__(self, _id):
        # ダンジョンの情報
        self.__id: int = _id
        self.__name = 'HOGE DUNGEON'

        self.__FLOOR_NUMBERS: int = 5
        self.__floors: list[Floor] = self.generate_floors(self.__FLOOR_NUMBERS)

        self.__now_floor_index: int = 0
        self.__turn: int = 1


        # マネージャー
        self.__floor_manager: Floor_manager
        self.__player_manager: Player_manager = None
        self.__enemy_manager_list: list[Enemy_manager] = []

        # ツール
        self.__camera = Camera()
        self.__display = Display.get_instance()


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

        # 音楽一時停止
        pyxel.stop()

        # 階段の効果音
        pyxel.play(0, 30, loop=False)

        # bgm再生
        pyxel.playm(0, loop=True)

        self.__now_floor_index += 1

        self.__camera.start_eye_catching(self.__name, self.__now_floor_index)
        # time.sleep(1)

        # self.__floors[self.__now_floor_index].__spawn_player()
        # self.__floors[self.__now_floor_index].spawn_steps()
        # self.__floors[self.__now_floor_index].spawn_enemys()
        # print('フロアスタートターン:', self.__turn)

        # manager
        self.__floor_manager = Floor_manager(self.__floors[self.__now_floor_index])
        if (self.__player_manager is None):
            self.__player_manager = Player_manager(self.__floor_manager.spawn_player())
        else:
            player = self.__floor_manager.spawn_player()
            player.set_status(
                self.__player_manager.character.name,
                self.__player_manager.character.level,
                self.__player_manager.character.hp,
                self.__player_manager.character.max_hp,
                self.__player_manager.character.mp,
                self.__player_manager.character.max_mp,
                self.__player_manager.character.attack,
                self.__player_manager.character.defense,
                self.__player_manager.character.exp
            )
            self.__player_manager = Player_manager(player)

        self.__display.show_status(
                self.__player_manager.character.name,
                self.__player_manager.character.level,
                self.__player_manager.character.hp,
                self.__player_manager.character.max_hp,
                self.__player_manager.character.mp,
                self.__player_manager.character.max_mp,
                self.__player_manager.character.attack,
                self.__player_manager.character.defense,
                self.__player_manager.character.exp
        )

        self.__floor_manager.set_layer_player(self.__player_manager.character)

        enemys = self.__floor_manager.spawn_enemys()
        self.__enemy_manager_list: list[Enemy_manager] = []
        for i, enemy in enumerate(enemys):
            enemys[i].target = self.__player_manager.character
            self.__enemy_manager_list.append(Enemy_manager(enemy))

        print('このフロアの敵の数', len(enemys))

        self.camera_show()
        self.__camera.clear_map()

        # self.__floor_manager.generate_enemy_layers(len(enemys))
        # for k in range(len(self.__floor_manager.floor.rooms)):
        #     for j in range(len(self.__floor_manager.floor.rooms)):
        #         print('enemylayers', k, j, '個数', len(self.__floor_manager.floor.rooms[k][j].layers.enemy_layers))

    # ターンを進める
    def forward_turn(self):

        self.__alive_check()

        if  (not pyxel.btnp(pyxel.KEY_SHIFT) and
            (pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_W)
             or pyxel.btnp(pyxel.KEY_S)  or pyxel.btnp(pyxel.KEY_E))):

            self.player_turn()
            self.enemys_turn()

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
                self.__floor_manager.clean_enemy_layer(i)
                del self.__enemy_manager_list[i]
                return

    def __clean_floor(self):
        # if (self.__player_manager.character.action == 'move'):
        #     self.__floor_manager.clean_player_layer()

        for i, enemy_manager in enumerate(self.__enemy_manager_list):
            # if (enemy_manager.character.action == 'move'):
            self.__floor_manager.clean_enemy_layer(i)

    # 入力されたキーをチェックする
    # 現在は方向キーだけ実装済み
    def player_turn(self):
        # TODO: 0829 プレイヤーが動いた後に、エネミーが動くようにしたい。

        self.__player_manager.get_input()
        player_want_to_move_position:list = self.__player_manager.get_want_to_move_room_address_and_position()
        if (self.__player_manager.character.action != 'none'):
            self.__turn += 1
            print('ターン:', self.__turn)

            if (self.__player_manager.character.action == 'attack'):
                exp = self.__floor_manager.attack_enemy(player_want_to_move_position[0], player_want_to_move_position[1], self.__player_manager.character.attack, self.__player_manager.character.name)
                is_level_up = self.__player_manager.add_exp_machine(exp)
                display = Display.get_instance()

                if (exp == -1):
                    display.show_fool_battle_message(self.__player_manager.character.name)
                # elif (is_level_up):
                #     display.show_level_up(self.__player_manager.character.name, )

                # else :
                #     self.__player_manager.character.exp += exp
                #     print('exp',self.__player_manager.character.exp)

            elif (self.__floor_manager.is_can_move_neo(player_want_to_move_position[0], player_want_to_move_position[1])):
                self.__floor_manager.clean_player_layer()
                # self.__floor_manager.clean_floor()
                self.__player_manager.set_position(room_address=player_want_to_move_position[0], position=player_want_to_move_position[1])
                self.__floor_manager.set_layer_player(self.__player_manager.character)

        self.__player_manager.print_status()

    def enemys_turn(self):
        for index, enemy_manager in enumerate(self.__enemy_manager_list):

            enemy_want_to_move_position:list = enemy_manager.get_want_to_move_room_address_and_position()

            enemy_manager.get_input()
            # 行き止まりに行こうとしたら、考えを改めてもらう(行き止まりじゃない選択肢が出るまでループ)
            if (enemy_manager.character.action == 'attack'):
                self.__floor_manager.attack_player(enemy_want_to_move_position[0], enemy_want_to_move_position[1], enemy_manager.character.attack, enemy_manager.character.name)
                # self.__display.show_attack_message(enemy_manager.character.name)
                continue

            for j in range(100):
                enemy_manager.get_input()
                enemy_want_to_move_position:list = enemy_manager.get_want_to_move_room_address_and_position()
                if (self.__floor_manager.is_can_move_neo(enemy_want_to_move_position[0], enemy_want_to_move_position[1])):
                    # if (enemy_manager.character.action == 'move'):
                    self.__floor_manager.clean_enemy_layer(index)
                    enemy_manager.set_position(room_address=enemy_want_to_move_position[0], position=enemy_want_to_move_position[1])
                    self.__floor_manager.set_layer_enemy(enemy_manager.character, index)
                    break


    def camera_show(self):
        self.__camera.target = self.__floor_manager.get_player_room_data(self.__player_manager.character)
        self.__camera.floor_rooms_data = self.__floor_manager.get_floor_rooms_data()
        self.__camera.show()
