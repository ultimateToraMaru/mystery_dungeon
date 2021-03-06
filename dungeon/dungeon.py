import time
from dungeon.room.object_layers.objects.food import Food
from dungeon.room.object_layers.objects.item import Item
from dungeon.room.object_layers.objects.trap import Trap
from tools.windows.menu_window import Menu_window
from dungeon.room.object_layers.objects.orange import Orange
from manager.enemy_manager import Enemy_manager
from manager.player_manager import Player_manager
from manager.character_manager import Character_manager
from manager.floor_manager import Floor_manager
from tools.display import Display
from tools.camera import Camera
from dungeon.floor import Floor
import pyxel
import pygame


class Dungeon:
    def __init__(self, _id):
        # ダンジョンの情報
        self.__id: int = _id
        self.__name = 'JEWELRY TOWER'

        self.__FLOOR_NUMBERS: int = 5   # 階数
        self.__floors: list[Floor] = self.generate_floors(self.__FLOOR_NUMBERS+1)

        self.__now_floor_number: int = 0
        self.__turn: int = 1


        # マネージャー
        self.__floor_manager: Floor_manager
        self.__player_manager: Player_manager = None
        self.__enemy_manager_list: list[Enemy_manager] = []
        self.__traps: list[Trap] = []

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

    def start_turn(self):
        """
        フロア到着時に一回だけ呼び出される
        ターンの始まりに先立ち、準備を行うメソッド
        """
        # self.__now_floor = self.get_next_floor()

        # 音楽一時停止
        pyxel.stop()

        # 階段の効果音
        pyxel.play(0, 30, loop=False)

        # bgm再生
        pyxel.playm(0, loop=True)

        self.__now_floor_number += 1



        self.__camera.start_eye_catching(self.__name, self.__now_floor_number)

        # manager
        try :
            self.__floor_manager = Floor_manager(self.__floors[self.__now_floor_number])

        except IndexError as e:
            self.__camera.show_game_clear()
            self.__display.show_game_clear(self.__player_manager.character.name, self.__name)
            # return

        # 1階のとき
        if (self.__player_manager is None):
            self.__player_manager = Player_manager(self.__floor_manager.spawn_player())

        # 2階以上の時(前の階のプレイヤーステータスを受け継ぐ)
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
                self.__player_manager.character.exp,
                self.__player_manager.character.pocket
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

        # エネミーを誕生させて、マネージャーにセット
        enemys = self.__floor_manager.spawn_enemys()
        self.__enemy_manager_list: list[Enemy_manager] = []
        for i, enemy in enumerate(enemys):
            enemys[i].target = self.__player_manager.character
            self.__enemy_manager_list.append(Enemy_manager(enemy, self.__now_floor_number))

        # トラップを誕生させて、ターゲットをセット
        self.__traps = self.__floor_manager.spawn_traps()
        for i, trap in enumerate(self.__traps):
            trap.target = self.__player_manager.character

        self.camera_show()
        self.__camera.clear_map()

        # ポケットの中身の参照をカメラに渡す
        self.__camera.set_pocket_contents(self.__player_manager.look_pocket())

    # def start_up_player_manager(self):

    # ターンを進める
    def forward_turn(self):
        """
        ターンを進める
        """
        if (self.__player_manager.character.alive == True and self.__FLOOR_NUMBERS+1 != self.__now_floor_number):
            self.__alive_check()

            # いずれかのボタンが押されたらターンを進める
            if  ((pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_W) or pyxel.btnp(pyxel.KEY_S)
                # or pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.KEY_E) or pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_C)
                or pyxel.btnp(pyxel.KEY_R))):

                self.player_turn()

                # SHIFTキーが押されていたらエネミーのターンは来ない
                keys=pygame.key.get_pressed()
                if (not keys[pygame.K_LSHIFT]):
                    self.enemys_turn()

                self.__traps_turn()

            # プレイヤーが階段の上にいるかチェックする
            if (self.__floor_manager.is_player_on_steps(self.__player_manager.character) == True):
                self.start_turn()



    def __alive_check(self):
        """
        プレイヤーとエネミーが生きているかチェックする。
        """

        # playerが死んだら、マネージャーはお役御免
        # if (self.__player_manager.character.alive == False):
        #     del self.__player_manager
        #     print('********** GAME OVER **********')
        #     return

        for i, enemy_manager in enumerate(self.__enemy_manager_list):
            # enemyが死んだら、マネージャーはお役御免
            if (enemy_manager.character.alive == False):

                # 対象enemyのレイヤーを掃除する
                self.__floor_manager.clean_enemy_layer(i)

                # 対象enemyのマネージャーを削除する
                del self.__enemy_manager_list[i]
                return

    def __clean_floor(self):
        """フロアをきれいにする
        """
        # if (self.__player_manager.character.action == 'move'):
        #     self.__floor_manager.clean_player_layer()

        for i, enemy_manager in enumerate(self.__enemy_manager_list):
            # if (enemy_manager.character.action == 'move'):
            self.__floor_manager.clean_enemy_layer(i)

    def player_turn(self):
        """プレイヤーのターン
        """

        self.__player_manager.get_input()
        player_want_to_move_position:list = self.__player_manager.get_want_to_move_room_address_and_position()

        obj = self.__floor_manager.check(self.__player_manager.character.room_address, self.__player_manager.character.position)
        if (type(obj) == Orange):
            self.__player_manager.pick_up(obj)

        # print('あしもと', obj)
        # print('pocket', self.__player_manager.look_pocket())

        if (self.__player_manager.character.action != 'none'):
            self.__turn += 1
            print('ターン:', self.__turn)


            if (self.__player_manager.character.action == 'attack'):
                exp = self.__floor_manager.attack_enemy(player_want_to_move_position[0], player_want_to_move_position[1], self.__player_manager.character.attack, self.__player_manager.character.name)
                is_level_up = self.__player_manager.add_exp_machine(exp)
                display = Display.get_instance()

                # TODO: なぜか空振りしていないのに、空振り判定がでてきまう。いったん保留。
                # if (exp == -1):
                #     display.show_fool_battle_message(self.__player_manager.character.name)

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
        self.__camera.set_floor_rooms_data(self.__floor_manager.get_floor_rooms_data())
        result = self.__camera.stand_by()
        self.__check_camera_result(result)

        # プレイヤーが死んだらゲームオーバー
        if (self.__player_manager.character.alive == False):
            self.__camera.show_game_over()
            self.__display.show_game_over(self.__player_manager.character.name, self.__name)

        if (self.__FLOOR_NUMBERS+1 == self.__now_floor_number):
            self.__camera.show_game_clear()
            self.__display.show_game_clear(self.__player_manager.character.name, self.__name)

        return result

    def __check_camera_result(self, result):
        # アイテムを使う時の処理

        # ポケットの食べ物を食べるとき
        if (isinstance(result, Food)):
            new_status = result.eat(self.__player_manager.get_status())
            self.__player_manager.character.pocket.remove_item(result)
            self.__player_manager.set_status(new_status)


    def __traps_turn(self):
        for i, trap in enumerate(self.__traps):
            if(trap.check_target() == True):
                trap.activate()