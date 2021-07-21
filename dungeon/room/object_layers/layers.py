from dungeon.room.object_layers.player_layer import Player_layer
from dungeon.room.object_layers.terrain_layer import Terrain_layer

# roomが持つオブジェクト(Terrain, Item, Player ...)を集約して持つクラス
class Layers:
    def __init__(self, type, is_player_room):
        self.__terrain_layer = Terrain_layer(type)
        self.__player_layer = Player_layer(is_player_room)

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