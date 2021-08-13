
# floor内の一個一個の部屋を表すクラス
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.enemy import Enemy
from dungeon.room.object_layers.objects.steps import Steps
from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.const.size import Size
import random
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.room.object_layers.layers import Layers


class Room:
    def __init__(self, type):
        self.__type = type
        self.__layers = Layers(type)
        # self.__is_start_room = is_start_room

        # roomはfloor内での自分自身の座標を持つべき。いらないかも?無駄かも？
        # self.__i = 0
        # self.__j = 0

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
    def type(self):
        pass

    @type.getter
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type
    
    # 部屋内のランダムな場所に階段を設置する
    def generate_steps(self, i, j):
        steps: Steps
        while (True):
            r_x = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
            r_y = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
            if (type(self.__layers.terrain_layer.data[r_x][r_y]) == Tile):
                # self.__layers.steps_layer.steps_position = [r_x, r_y]
                steps = Steps(room_address=[i, j], position=[r_x, r_y])
                self.__layers.steps_layer.data[r_x][r_y] = steps
                break
        return steps

    # 部屋内のランダムな場所にランダムな数のエネミーを設置する
    def generate_enemys(self, i, j):
        enemy_nums = random.randint(1, 5)
        # enemy_nums = 1
        enemys = []
        # ランダムな場所に生成
        for index in range(enemy_nums):
            r_x = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
            r_y = random.randint(0, Size.MAX_MASS_IN_ROOM_ONE_SIDE-1)
            if (type(self.__layers.terrain_layer.data[r_x][r_y]) == Tile and 
                type(self.__layers.player_layer.data[r_x][r_y]) == None_obj and 
                type(self.__layers.steps_layer.data[r_x][r_y]) == None_obj and 
                type(self.__layers.enemy_layer.data[r_x][r_y]) == None_obj):

                enemy = Enemy(Color.BLACK, room_address=[i, j], position=[r_x, r_y])
                self.__layers.enemy_layer.data[r_x][r_y] = enemy
                enemys.append(enemy)

        return enemys

    # 部屋の中心にプレイヤーを設置する
    def generate_player(self, i, j):
        player = Player(Color.BLACK, room_address=[i, j], position=[5, 5])
        return player
    
    # # ??? プレイヤーが階段に到着したか確認する
    # def steps_check(self):
    #     for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
    #         for j in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
    #             if (type(self.__layers.player_layer.data[i][j]) == Player and
    #                 type(self.__layers.steps_layer.data[i][j]) == Steps):
    #                 return True

    #     return False
    
    # 与えられた座標(x, y)の場所に、障害となるオブジェクト(敵、壁、プレイヤー)がないか判定する(ない: true, ある: false)
    # バグは個々のメソッドが原因そう
    def is_noneobj(self, x, y):
        print('移動しようとしているマスの状態 terrain:', type(self.layers.terrain_layer.data[x][y]), 'player:', type(self.layers.player_layer.data[x][y]), 'enemy:', type(self.layers.enemy_layer.data[x][y]))
        return (type(self.layers.terrain_layer.data[x][y]) == Tile and 
                type(self.layers.player_layer.data[x][y]) == None_obj and 
                type(self.layers.enemy_layer.data[x][y]) == None_obj)