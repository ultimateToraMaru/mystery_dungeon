from tools.menu_window import Menu_window
from tools.display_floor_index import Display_floor_index
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj
import time
import pyxel

class Map_window():
    def __init__(self):
        self.__is_show = False
        self.__floor_rooms_data = []
        self.__map_indexes = [[0, 0, 0, 0]]

    @property
    def is_show(self):
        pass

    @is_show.setter
    def is_show(self, is_show):
        self.__is_show = is_show

    @is_show.getter
    def is_show(self):
        return self.__is_show

    @property
    def floor_rooms_data(self):
        pass

    @floor_rooms_data.setter
    def floor_rooms_data(self, floor_rooms_data):
        self.__floor_rooms_data = floor_rooms_data

    # 全体マップ
    def show(self):
        # # 真っ黒で上書きする
        # pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        # マップに追加された部屋を写しだす
        for index in range(len(self.__map_indexes)):
            print(self.__map_indexes)
            map_index = self.__map_indexes[index]
            self.__floor_rooms_data[map_index[0]][map_index[1]].layers.terrain_layer.draw(map_index[2], map_index[3], size=5)
            self.__floor_rooms_data[map_index[0]][map_index[1]].layers.steps_layer.draw(map_index[2], map_index[3], size=5)
            self.__floor_rooms_data[map_index[0]][map_index[1]].layers.player_layer.draw(map_index[2], map_index[3], size=5)


    # 末尾の座標がすでにappendされたものかどうか判断しながらappendしていく
    def add_map(self, target):
        for i in range(len(self.__floor_rooms_data)):
            for j in range(len(self.__floor_rooms_data)):
                x = i*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                y = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE

                # 全マップ表示
                # self.__map_indexes.append([i, j, x, y])

                # playerがいるお部屋をマップに追加する
                if (target.room_address == [i, j]):
                    if (self.__map_indexes[-1] != [i, j, x, y]):
                        self.__map_indexes.append([i, j, x, y])

    def clear_map(self, target):
        self.__map_indexes = [[ target.room_address[0],
                                target.room_address[1],
                                target.room_address[0]*Size.MAX_MASS_IN_ROOM_ONE_SIDE,
                                target.room_address[1]*Size.MAX_MASS_IN_ROOM_ONE_SIDE]]

        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)