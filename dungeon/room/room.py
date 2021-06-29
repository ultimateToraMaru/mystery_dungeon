
# floor内の一個一個の部屋を表すクラス
from dungeon.room.object_layers.layers import Layers


class Room:
    def __init__(self):
        self.__room_objects = Layers()

    # # terrainのプロパティ
    @property
    def room_objects(self):
        pass

    @room_objects.getter
    def room_objects(self):
        return self.__room_objects

    @room_objects.setter
    def room_objects(self, room_objects):
        self.__room_objects = room_objects