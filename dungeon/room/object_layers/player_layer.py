from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.objects.player import Player
import math
from dungeon.const.properties import Properties
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Player_layer():
    def __init__(self, is_start_room):
        self.__data = [[None_obj(Color.BLACK)] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)]      
        
        if (is_start_room):
            # print('start')
            self.__player = Player(Color.SKYPINK)

    def draw(self, room_x, room_y):
        for x in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
            for y in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[x][y].create(x+room_x, y+room_y)

    def get_player_position(self):
        return self.__player.position
    
    def set_player_position(self, x, y):
        self.__player.position = [x, y]
    

    # なんか同時に複数の部屋に現れちゃう。だけどプレイやーを配置で来た！すいごい！すー
    def set_start_position(self):
        r_i = random.randint(0, len(self.__data)-1)
        r_j = random.randint(0, len(self.__data)-1)

        self.__player.position = [r_i, r_j]
        self.__data[r_j][r_j] = self.__player
