from dungeon.room.object_layers.terrain_layer import Terrain_layer

# roomが持つオブジェクト(Terrain, Item, Player ...)を集約して持つクラス
class Layers:
    def __init__(self, type):

        if  (type == 'normal'):
            self.__terrain_layer = Terrain_layer('normal')
        elif (type == 'none'):
            self.__terrain_layer = Terrain_layer('none')

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
    def terrain_layer(self, terrain_layer):
        self.__terrain_layer = terrain_layer