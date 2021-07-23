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
        self.__data = [[None_obj()] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)] 
        for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
            for j in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[i][j] = None_obj()

        self.__tmp_player_position = [0, 0]

        if (is_start_room):
            self.__player = Player(Color.SKYPINK)
        else:
            self.__player = None_obj()


    @property
    def data(self):
        pass

    @data.getter
    def data(self):
        return self.__data


    def draw(self, room_x, room_y):
        # print(room_x, room_y)
        # print(self.__data[self.__player_position[0]][self.__player_position[1]])
        for x in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
            for y in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[x][y].create(x+room_x, y+room_y)

    def get_player_position(self):
        return self.__player.position
    
    def set_player_position(self, x, y):
        self.__tmp_player_position = [x, y]
        self.__player.position = [x, y]
    
    # なんか同時に複数の部屋に現れちゃう。だけどプレイやーを配置で来た！すごい！すー
    def set_start_position(self):
        # r_i = random.randint(0, len(self.__data)-1)
        # r_j = random.randint(0, len(self.__data)-1)

        # ランダムじゃなくて、部央でもよくない？
        # しかも、中央は絶対部屋になってるぜよ
        r_i = math.floor(Properties.MAX_MASS_IN_ROOM_ONE_SIDE/2) 
        r_j = math.floor(Properties.MAX_MASS_IN_ROOM_ONE_SIDE/2) 

        # self.__player.position = [r_i, r_j]
        self.set_player_position(r_i, r_j)
        self.__data[self.__player.position[0]][self.__player.position[1]] = self.__player
      
        print('部屋内位置', r_i, r_j)
        # print(self.__data[r_i][r_j])
        # print(self.__data)

        return self.__player

    def set_position(self):
        # print(self.__tmp_player_position, self.__player.position)
        self.__data[self.__tmp_player_position[0]][self.__tmp_player_position[1]] = None_obj()
        self.__data[self.__player.position[0]][self.__player.position[1]] = self.__player
        self.set_player_position(self.__player.position[0], self.__player.position[1])
        
        # print(self.__data)
