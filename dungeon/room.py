
# floor内の一個一個の部屋を表すクラス
from dungeon.objects.wall import Wall


class Room:
    def __init__(self):
        self.__MAXMASS = 10                                                         # 部屋の一辺の最大マス数を表す変数
        self.__terrain = [[0] * self.__MAXMASS for i in range(self.__MAXMASS)]      # 地形データを表す変数
        self.__terrain = self.generate_terrain(self.__MAXMASS, self.__terrain)

    # terrainのプロパティ
    @property
    def terrain(self):
        pass

    @terrain.getter
    def terrain(self):
        return self.__terrain

    @terrain.setter
    def terrain(self, terrain):
        self.__terrain = terrain

    # 地形をランダムで形成する関数
    def generate_terrain(self, MAXMASS, terrain):

        # まずは四方に壁を作る
        for i in range(MAXMASS):
            terrain[0][i] = Wall()
            terrain[i][0] = Wall()
            terrain[MAXMASS-1][i] = Wall()
            terrain[i][MAXMASS-1] = Wall()
            # 1じゃなくて直接配列の中にオブジェクト(壁オブジェクト)とかを入れれば、いいんじゃない？　by 06/21 22:40

        return terrain

    