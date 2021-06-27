
# floor内の一個一個の部屋を表すクラス
from dungeon.objects.room_objects import Room_objects


class Room:
    def __init__(self):
        self.__room_objects = Room_objects()

        # # 地形データ(木や壁)や落ちてるアイテム(アイテムは取得したら床オブジェクトを設置)を表す変数
        # # そうすればterrain_dataとterrainを分ける必要はない！
        # self.__terrain_data = [[Tile(Color.BLACK)] * self.__MAXMASS for i in range(self.__MAXMASS)]      
        # self.__terrain_data = self.generate_terrain_data(self.__terrain_data, self.__MAXMASS)

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

    # # 地形をランダムで形成する関数
    # def generate_terrain_data(self, terrain_data, MAXMASS):
    #     # self.__terrain_data[0][0] = Wall(Color.RED)
    #     # まずは四方に壁を作る
    #     for i in range(MAXMASS):
    #         terrain_data[0][i] = Wall(Color.RED)
    #         terrain_data[i][0] = Wall(Color.RED)
    #         terrain_data[MAXMASS-1][i] = Wall(Color.RED)
    #         terrain_data[i][MAXMASS-1] = Wall(Color.RED)
    #         # 1じゃなくて直接配列の中にオブジェクト(壁オブジェクト)とかを入れれば、いいんじゃない？ by 06/21 22:40

    #     return terrain_data
