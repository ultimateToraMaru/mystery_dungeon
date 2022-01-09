# floor内の一個一個の部屋を表すクラス
from dungeon.room.object_layers.objects.attack_effect import Attack_effect
from dungeon.room.object_layers.enemy_layer import Enemy_layer
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.enemy import Enemy
from dungeon.room.object_layers.objects.orange import Orange
from dungeon.room.object_layers.objects.steps import Steps
from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.const.size import Size
import random
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.tile_path import Tile_path
from dungeon.room.object_layers.objects.tile_room import Tile_room
from dungeon.room.object_layers.objects.trap import Trap
from dungeon.room.object_layers.objects.trap_damage import Trap_damage
from dungeon.room.object_layers.objects.trap_warp import Trap_warp
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.room.object_layers.layers import Layers


class Room:
    def __init__(self, is_room, path_way_type, room_address):
        self.__is_room = is_room
        self.__layers = Layers(is_room, path_way_type)
        self.__room_address = room_address

    @property
    def layers(self):
        pass

    @layers.getter
    def layers(self):
        return self.__layers

    @layers.setter
    def layers(self, layers):
        self.__layers = layers

    @property
    def is_room(self):
        pass

    @is_room.getter
    def is_room(self):
        return self.__is_room

    @is_room.setter
    def is_room(self, is_room):
        self.__is_room = is_room

    @property
    def room_address(self):
        pass

    @room_address.getter
    def room_address(self):
        return self.__room_address

    @room_address.setter
    def room_address(self, room_address):
        self.__room_address = room_address

    # 部屋内のランダムな場所に階段を設置する
    def generate_steps(self, r_x, r_y):
        steps: Steps
        while (True):
            p_x = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
            p_y = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)

            if (type(self.__layers.terrain_layer.data[p_x][p_y]) == Tile_room):
                #isinstance(type(self.__layers.terrain_layer.data[p_x][p_y]), Tile_room)):
                # self.__layers.steps_layer.steps_position = [r_x, r_y]
                steps = Steps(room_address=[r_x, r_y], position=[p_x, p_y])
                self.__layers.steps_layer.data[p_x][p_y] = steps
                break
        return steps

    # 部屋内のランダムな場所にランダムな数のエネミーを設置する
    def generate_enemys(self, total_enemy_nums):
        enemy_nums = random.randint(1, 5)
        # enemy_nums = 1
        enemys = []

        # 今まで生成されたエネミー分のレイヤーを作っておく
        for i in range(total_enemy_nums):
            self.__layers.enemy_layers.append(Enemy_layer())

        # ランダムな場所に生成
        for i in range(enemy_nums):
            p_x = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
            p_y = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)

            if (self.is_noneobj(p_x, p_y)):

                enemy = Enemy(Color.BLACK, room_address=[self.__room_address[0],self.__room_address[1]], position=[p_x, p_y])


                enemy_layer = Enemy_layer()
                enemy_layer.data[p_x][p_y] = enemy
                self.__layers.enemy_layers.append(enemy_layer)

                enemys.append(enemy)

        return enemys

    # 部屋の中心にプレイヤーを設置する
    def generate_player(self, r_x, r_y):
        player = Player(Color.BLACK, room_address=[r_x, r_y], position=[5, 5])
        return player

    def generate_attack_effect(self, p_x, p_y):
        attack_effect = Attack_effect(room_address=self.__room_address, position=[p_x, p_y], isMove=False)
        return attack_effect

    def generate_items(self):
        p_x = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
        p_y = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)

        # orange: Orange
        if (self.is_noneobj_in_room(p_x, p_y)):
            orange = Orange(Color.BLACK)
            self.__layers.item_layer.data[p_x][p_y] = orange

        # return orange

    def generate_traps(self, trap_nums):
        traps: list[Trap] = []

        # ランダムな場所に生成
        for i in range(trap_nums):

            p_x = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
            p_y = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)

            if (self.is_noneobj_in_room(p_x, p_y)):
                # trap = Trap_damage(room_address=self.__room_address, position=[p_x, p_y])
                trap = Trap_warp(room_address=self.__room_address, position=[p_x, p_y])
                self.__layers.trap_layer.data[p_x][p_y] = trap

                traps.append(trap)
        #         break
        return traps

    # 与えられた座標(x, y)の場所に、障害となるオブジェクト(敵、壁、プレイヤー)がないか判定する(ない: true, ある: false)
    # バグは個々のメソッドが原因そう
    def is_noneobj(self, p_x, p_y):
        # print('移動しようとしているマス', [p_x, p_y], 'の状態 terrain:', type(self.layers.terrain_layer.data[p_x][p_y]), 'player:', type(self.layers.player_layer.data[p_x][p_y]), 'enemy:', type(self.layers.enemy_layer.data[p_x][p_y]))
        if ((type(self.layers.terrain_layer.data[p_x][p_y]) == Tile_room
            or type(self.layers.terrain_layer.data[p_x][p_y]) == Tile_path)
            and type(self.layers.player_layer.data[p_x][p_y]) == None_obj):

            for i in range(len(self.__layers.enemy_layers)):
                if (type(self.__layers.enemy_layers[i].data[p_x][p_y]) != None_obj):
                    return False

            return True

        return False

    def is_noneobj_in_room(self, p_x, p_y):
        # print('移動しようとしているマス', [p_x, p_y], 'の状態 terrain:', type(self.layers.terrain_layer.data[p_x][p_y]), 'player:', type(self.layers.player_layer.data[p_x][p_y]), 'enemy:', type(self.layers.enemy_layer.data[p_x][p_y]))
        if (type(self.layers.terrain_layer.data[p_x][p_y]) == Tile_room
            and type(self.layers.player_layer.data[p_x][p_y]) == None_obj):

            for i in range(len(self.__layers.enemy_layers)):
                if (type(self.__layers.enemy_layers[i].data[p_x][p_y]) != None_obj):
                    return False

            return True

        return False

    def get_obj(self, x, y):
        return self.layers.item_layer.data[x][y]