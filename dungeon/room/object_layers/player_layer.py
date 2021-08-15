from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.player import Player
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Player_layer():
    def __init__(self):
        self.__data = [[None_obj()] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]
        for p_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for p_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[p_x][p_y] = None_obj()

    @property
    def data(self):
        pass

    @data.getter
    def data(self):
        return self.__data

    @property
    def player(self):
        pass

    @player.setter
    def player(self, player):
        self.__player = player


    def draw(self, p_x, p_y):
        for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[r_x][r_y].create(r_x+p_x, r_y+p_y)

    # def get_player_position(self):
    #     return self.__player.position
    
    def set_start_position(self, player):
        # r_i = random.randint(0, len(self.__data)-1)
        # r_j = random.randint(0, len(self.__data)-1)

        # ランダムじゃなくて、部央でもよくない？
        # しかも、中央は絶対部屋になってるぜよ
        p_x = math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2) 
        p_y = math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2) 

        self.set_player_position(player, p_x, p_y)
        self.__data[player.position[0]][player.position[1]] = player

        return player

    def set_position(self, player):
        self.__data[player.tmp_position[0]][player.tmp_position[1]] = None_obj()
        self.__data[player.position[0]][player.position[1]] = player
        player.tmp_position = [player.position[0], player.position[1]]
        player.position = [player.position[0], player.position[1]]
    
    # プレイヤーの残像をきれいに掃除する
    def clean(self):
        for p_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for p_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[p_x][p_y] = None_obj()
