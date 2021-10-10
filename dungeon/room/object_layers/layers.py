from dungeon.room.object_layers.effect_layer import Effect_layer
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
    def __init__(self, type):
        self.__terrain_layer = Terrain_layer(type)
        self.__player_layer = Player_layer()
        self.__steps_layer = Steps_layer()
        # self.__enemy_layer = Enemy_layer()
        self.__enemy_layers: list[Enemy_layer] = []
        self.__effect_layer = Effect_layer()
        print('layers')


    # def create_enemy_layers(self, enemy_nums_in_floor):
    #     for i in range(enemy_nums_in_floor):
    #         self.__enemy_layers = Enemy_layer()
    #         # print(i)

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
    def enemy_layers(self):
        pass

    @enemy_layers.getter
    def enemy_layers(self):
        return self.__enemy_layers

    @enemy_layers.setter
    def enemy_layers(self, enemy_layers):
        self.__enemy_layers = enemy_layers


    @property
    def effect_layer(self):
        pass

    @effect_layer.getter
    def effect_layer(self):
        return self.__effect_layer

    @effect_layer.setter
    def effect_layer(self, effect_layer):
        self.__effect_layer = effect_layer