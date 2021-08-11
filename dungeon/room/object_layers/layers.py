from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.room.object_layers.enemy_layer import Enemy_layer
from dungeon.room.object_layers.objects.steps import Steps
from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.steps_layer import Steps_layer
from dungeon.room.object_layers.player_layer import Player_layer
from dungeon.room.object_layers.terrain_layer import Terrain_layer

# roomが持つオブジェクト(Terrain, Item, Player ...)を集約して持つクラス
class Layers:
    def __init__(self, type, is_start_room):
        self.__terrain_layer = Terrain_layer(type)
        self.__player_layer = Player_layer(is_start_room)
        self.__steps_layer = Steps_layer()
        self.__enemy_layer = Enemy_layer()

        # if (is_start_room):
        #     self.__player_layer = Player_layer(True)
        # else:
        #     self.__player_layer = Player_layer(False)
        # self.__item

    @property
    def terrain_layer(self):
        pass

    @terrain_layer.getter
    def terrain_layer(self):
        return self.__terrain_layer

    @terrain_layer.setter
    def terrain_layer(self, terrain_layer):
        self.__terrain_layer = terrain_layer
    
    @property
    def player_layer(self):
        pass

    @player_layer.getter
    def player_layer(self):
        return self.__player_layer

    @player_layer.setter
    def player_layer(self, player_layer):
        self.__player_layer = player_layer

    
    @property
    def steps_layer(self):
        pass

    @steps_layer.getter
    def steps_layer(self):
        return self.__steps_layer

    @steps_layer.setter
    def steps_layer(self, steps_layer):
        self.__steps_layer = steps_layer

    
    @property
    def enemy_layer(self):
        pass

    @enemy_layer.getter
    def enemy_layer(self):
        return self.__enemy_layer

    @enemy_layer.setter
    def enemy_layer(self, enemy_layer):
        self.__enemy_layer = enemy_layer
    
    def is_noneobj(self, x, y):
        # エネミーがすり抜けてしまう。すり抜けたうえで、次の部屋に移動しようとした際にエラーが吐かれる
        return (type(self.__terrain_layer.data[x][y]) == Tile and type(self.__player_layer.data[x][y]) == None_obj and type(self.__enemy_layer.data[x][y]) == None_obj)