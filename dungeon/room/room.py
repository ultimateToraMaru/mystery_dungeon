
# floor内の一個一個の部屋を表すクラス
from dungeon.color import Color
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.room.object_layers.layers import Layers


class Room:
    def __init__(self, type):
        if  (type == 'normal'):
            self.__layers = Layers('normal')
        elif (type == 'none'):
            self.__layers = Layers('none')

    # # terrainのプロパティ
    @property
    def layers(self):
        pass

    @layers.getter
    def layers(self):
        return self.__layers

    @layers.setter
    def layers(self, layers):
        self.__layers = layers