from dungeon.room.object_layers.objects.player import Player
import math
from dungeon.const.properties import Properties
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Player_layer():
    def __init__(self):
        self.__player = Player(Color.SKYPINK)
        self.__data = [[None] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)]      

    def draw(self, i, j, x, y):
        self.__data[i][j].create(x, y)

    def get_player_position(self):
        return self.__player.position
    
    def set_player_position(self, x, y):
        self.__player.position = [x, y]
