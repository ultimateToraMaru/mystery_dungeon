from dungeon.objects.objects_data.terrain import Terrain

# roomが持つオブジェクト(Terrain, Item, Player ...)を集約して持つクラス
class Room_objects:
    def __init__(self):
        self.__terrain = Terrain()
        # self.__item
        # self.__player

    # terrain_dataのプロパティ
    @property
    def terrain(self):
        pass

    @terrain.getter
    def terrain(self):
        return self.__terrain

    @terrain.setter
    def terrain(self, terrain):
        self.__terrain = terrain