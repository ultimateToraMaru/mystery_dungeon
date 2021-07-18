
# floor内の一個一個の部屋を表すクラス
from random import random
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.room.object_layers.layers import Layers


class Room:
    def __init__(self, type):
        self.__type = type
        self.__layers = Layers(type)

    @property
    def layers(self):
        pass

    @layers.getter
    def layers(self):
        return self.__layers

    @layers.setter
    def layers(self, layers):
        self.__layers = layers
    
    @property
    def type(self):
        pass

    @type.getter
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type