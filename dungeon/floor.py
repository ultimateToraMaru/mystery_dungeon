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
    def rooms_terrain_draw(self):
        x = 0
        y = 0
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                x = i*Properties.MAX_MASS_IN_ROOM_ONE_SIDE
                y = j*Properties.MAX_MASS_IN_ROOM_ONE_SIDE
                self.__rooms[i][j].layers.terrain_layer.draw(x, y)
