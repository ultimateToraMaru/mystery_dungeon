from dungeon.room.object_layers.terrain_layer import Terrain_layer

# roomが持つオブジェクト(Terrain, Item, Player ...)を集約して持つクラス
class Layers:
    def __init__(self):
        self.__terrain_layer = Terrain_layer()
        # self.__item
        # self.__player

    # terrain_dataのプロパティ
    @property
    def terrain_layer(self):
        pass

    @terrain_layer.getter
    def terrain_layer(self):
        return self.__terrain_layer

    @terrain_layer.setter
    def terrain_layer(self, terrain):
        self.__terrain_layer = terrain