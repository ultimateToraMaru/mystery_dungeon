from dungeon.const.properties import Properties
from dungeon.room.room import Room
import random

# dungeonのfloorを表す関数。複数のroomを持つ
class Floor:
    def __init__(self):
        self.__rooms = [[Room('none', False)] * Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        for i in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
            for j in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                self.__rooms[i][j] = Room('none', False)

        self.__rooms = self.generate()
        self.__start_room_position = [0,0]

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
        r = random.randint(2, 5)    # rの範囲:2~5。お部屋の数。
        rooms = [[Room('none', False)] * Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE for i in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE)]
        for i in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
            for j in range(Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE):
                rooms[i][j] = Room('none', False)
        print('部屋の数', r)

        r_select_start_room = random.randint(0, r-1)    # startする部屋をランダムで選ぶ。上からr番目みたいな感じ。
        for i in range(r):
            r_x = random.randint(0, Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            r_y = random.randint(0, Properties.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-1) 
            # print(r_x, r_y)
            # print('i', i, 'r_start', r_select_start_room)
            if (i == r_select_start_room):
                print('start_room:', r_x, r_y)
                room = Room('normal', True)
                print('プレイヤーがいる部屋', room)
                rooms[r_x][r_y] = room
                self.__start_room_position = [r_x, r_y]
            else :
                non_room = Room('normal', False)
                print('プレイヤーがいない部屋', non_room)
                rooms[r_x][r_y] = non_room
        
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
        
        print(self.__rooms)
                
    
    def set_start_position(self):
        self.__rooms[self.__start_room_position[0]][self.__start_room_position[1]].layers.player_layer.set_start_position()

    # def select_start_room(self):
    #     r_room_i = random.randint(0, len(self.__rooms)-1)
    #     r_room_j = random.randint(0, len(self.__rooms)-1)
    #     print('部屋の選定', r_room_i, r_room_j)

    #     # self.__rooms[r_room_i][r_room_j].is_start_room = True
    #     self.__rooms[r_room_i][r_room_j].layers.player_layer.set_start_position()
    
    # def search_player(self):
    #     for i in range(len(self.__rooms)):
    #         for j in range(len(self.__rooms)):
    #             self.__rooms[i][j].layers.player_layer.get_player_position()
    
    # def player_move(self, direction):
    #     if (direction == 'right'):
    #         player_position = self.__player_layer.get_player_position()
    #         self.__player_layer.set_player_position(player_position[0], player_position[1]+1)

    # def room_pass_finding(self):
    #     for i in range(len(self.__rooms)):
    #         for j in range(len(self.__rooms)):
    #             if (self.__rooms[i][j].type == 'normal'):
    #                 self.__rooms[i][j].layers.terrain_layer.set_point()