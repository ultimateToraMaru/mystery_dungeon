from dungeon.room.room import Room
import random

# dungeonのfloorを表す関数。複数のroomを持つ
class Floor:
    def __init__(self):
        self.__MAX_BLOCKS = 5
        self.__rooms = [[Room('none')] * self.__MAX_BLOCKS for i in range(self.__MAX_BLOCKS)]
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

    def generate(self):
        r = random.randint(2, 5)    # rの範囲。1~5。お部屋の数。
        rooms = [[Room('none')] * self.__MAX_BLOCKS for i in range(self.__MAX_BLOCKS)]
        print('部屋の数', r)

        for i in range(r):
            r_x = random.randint(0, self.__MAX_BLOCKS-1) 
            r_y = random.randint(0, self.__MAX_BLOCKS-1) 
            print(r_x, r_y)
            rooms[r_x][r_y] = Room('normal')
        
        return rooms

    def rooms_terrain_draw(self):
        x = 0
        y = 0
        for i in range(len(self.__rooms)):
            for j in range(len(self.__rooms)):
                x = i*10
                y = j*10
                self.__rooms[i][j].layers.terrain_layer.draw(x, y)
