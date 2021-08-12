from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.player import Player
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Enemy_layer():
    def __init__(self):
        self.__data = [[None_obj()] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)] 
        for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for j in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[i][j] = None_obj()
        
        # self.__enemys = []
        # self.__enemys = enemys_generate()
        #self.__tmp_player_position = [0, 0]
        #


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


    def draw(self, room_x, room_y):
        # print(room_x, room_y)
        # print(self.__data[self.__player_position[0]][self.__player_position[1]])
        for x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[x][y].create(x+room_x, y+room_y)
    
    # def set_enemy_position(self, enemy, x, y):
    #     enemy.tmp_position = [x, y]
    #     enemy.position = [x, y]

    def set_position(self, enemy):
        # print(enemy.room_address, enemy.position)
        # print('set_position', enemy.position[0], enemy.position[1])
        self.__data[enemy.tmp_position[0]][enemy.tmp_position[1]] = None_obj()
        self.__data[enemy.position[0]][enemy.position[1]] = enemy
        enemy.tmp_position = [enemy.position[0], enemy.position[1]]
        enemy.position = [enemy.position[0], enemy.position[1]]
        # self.set_enemy_position(enemy, enemy.position[0], enemy.position[1])
        
    #     # print(self.__data)
    
    # エネミーの残像をきれいに掃除する
    def clean(self):
        for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for j in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[i][j] = None_obj()
