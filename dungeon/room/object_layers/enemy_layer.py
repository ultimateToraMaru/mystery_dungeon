from dungeon.display import Display
from dungeon.room.object_layers.objects.enemy import Enemy
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
        for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[r_x][r_y] = None_obj()

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
                self.__data[r_x][r_y].create(r_x+p_x, r_y+p_y, size=16)

    def set_position(self, enemy):
        # if (enemy.position[0] < 0 or 9 < enemy.position[0]):
        #     print('enemy.position[0]に異常な値がセットされました: ', enemy.room_address, enemy.position, 'エネミー: ', enemy)
        # elif (enemy.position[1] < 0 or 9 < enemy.position[1]):
        #     print('enemy.position[1]に異常な値がセットされました: ', enemy.room_address, enemy.position, 'エネミー: ', enemy)

        self.__data[enemy.tmp_position[0]][enemy.tmp_position[1]] = None_obj()
        self.__data[enemy.position[0]][enemy.position[1]] = enemy
        enemy.tmp_position = [enemy.position[0], enemy.position[1]]
        enemy.position = [enemy.position[0], enemy.position[1]]

    # エネミーの残像をきれいに掃除する
    def clean(self):
        for p_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            for p_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[p_x][p_y] = None_obj()

    def set_damage(self, p_x, p_y, damage_point, attacker_name):
        if (type(self.__data[p_x][p_y]) == Enemy):
            print('hit!')
            return self.__data[p_x][p_y].damage(damage_point, attacker_name)
        else :
            return -1
