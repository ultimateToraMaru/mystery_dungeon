from dungeon.const.properties import Properties
from dungeon.room.room import Room
import random

# dungeonのfloorを表す関数。複数のroomを持つ
class Floor:
    def __init__(self):
        self.__rooms = [[Room('none')] * Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        self.__rooms = self.generate()

    @property
    def rooms(self):
        pass

    @rooms.getter
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

    # ランダムな場所に部屋を生成
    def generate(self):
        r = random.randint(2, 5)    # rの範囲。2~5。お部屋の数。
        rooms = [[Room('none')] * Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        print('部屋の数', r)

        for i in range(r):
            r_x = random.randint(0, Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            r_y = random.randint(0, Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            print(r_x, r_y)
            rooms[r_x][r_y] = Room('normal')
        
        return rooms

    # 部屋の地形データを読み取り、オブジェクトにdrawの指示を出す
    def terrain_draw(self):
        x = 0
        y = 0
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                x = i*Properties.MAX_MASS_IN_ROOM_ONE_SIDE
                y = j*Properties.MAX_MASS_IN_ROOM_ONE_SIDE
                self.__rooms[i][j].layers.terrain_layer.draw(x, y)

    def player_draw(self):
        # if (direction == 'right'):
        #     player_position = self.__rooms.player_layer.get_player_position()
        #     self.__player_layer.set_player_position(player_position[0], player_position[1]+1)
        x = 0
        y = 0
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                x = i*Properties.MAX_MASS_IN_ROOM_ONE_SIDE
                y = j*Properties.MAX_MASS_IN_ROOM_ONE_SIDE
                self.__rooms[i][j].layers.player_layer.draw(x, y)
                
    def select_start_room(self):
        r_room_i = random.randint(0, len(self.__rooms)-1)
        r_room_j = random.randint(0, len(self.__rooms)-1)
        self.__rooms[r_room_i][r_room_j].layers.player_layer.set_start_position()
    
    
    def search_player(self):
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                self.__rooms[i][j].layers.player_layer.get_player_position()
    
    # def player_move(self, direction):
    #     if (direction == 'right'):
    #         player_position = self.__player_layer.get_player_position()
    #         self.__player_layer.set_player_position(player_position[0], player_position[1]+1)

    # def room_pass_finding(self):
    #     for i in range(len(self.__rooms)):
    #         for j in range(len(self.__rooms)):
    #             if (self.__rooms[i][j].type == 'normal'):
    #                 self.__rooms[i][j].layers.terrain_layer.set_point()