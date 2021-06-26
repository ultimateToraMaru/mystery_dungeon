
# floor内の一個一個の部屋を表すクラス
from dungeon.objects.tile import Tile
from dungeon.color import Color
from dungeon.objects.wall import Wall


class Room:
    def __init__(self):
        self.__MAXMASS = 10                                                         # 部屋の一辺の最大マス数を表す変数
        
        # 地形データ(木や壁)や落ちてるアイテム(アイテムは取得したら床オブジェクトを設置)を表す変数
        # そうすればroom_dataとterrainを分ける必要はない！
        self.__room_data = [[Tile(Color.BLACK)] * self.__MAXMASS for i in range(self.__MAXMASS)]      
        self.__room_data = self.generate_room_data(self.__room_data, self.__MAXMASS)

    # terrainのプロパティ
    @property
    def room_data(self):
        pass

    @room_data.getter
    def room_data(self):
        return self.__room_data

    @room_data.setter
    def room_data(self, room_data):
        self.__room_data = room_data

    # 地形をランダムで形成する関数
    def generate_room_data(self, room_data, MAXMASS):
        # self.__room_data[0][0] = Wall(Color.RED)
        # まずは四方に壁を作る
        for i in range(MAXMASS):
            room_data[0][i] = Wall(Color.RED)
            room_data[i][0] = Wall(Color.RED)
            room_data[MAXMASS-1][i] = Wall(Color.RED)
            room_data[i][MAXMASS-1] = Wall(Color.RED)
            # 1じゃなくて直接配列の中にオブジェクト(壁オブジェクト)とかを入れれば、いいんじゃない？ by 06/21 22:40
