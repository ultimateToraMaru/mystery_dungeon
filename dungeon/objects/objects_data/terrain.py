from dungeon.objects.tile import Tile
from dungeon.color import Color
from dungeon.objects.wall import Wall

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Terrain():
    def __init__(self):
        self.__MAXMASS = 10     # 部屋の一辺の最大マス数を表す変数
        # 地形データ(木や壁)や落ちてるアイテム(アイテムは取得したら床オブジェクトを設置)を表す変数
        # そうすればterrain_dataとterrainを分ける必要はない！
        self.__data = [[Tile(Color.BLACK)] * self.__MAXMASS for i in range(self.__MAXMASS)]      
        self.__data = self.generate(self.__data, self.__MAXMASS)

    # 地形をランダムで形成する関数
    def generate(self, data, MAXMASS):
        # self.__terrain_data[0][0] = Wall(Color.RED)
        # まずは四方に壁を作る
        for i in range(MAXMASS):
            data[0][i] = Wall(Color.RED)
            data[i][0] = Wall(Color.RED)
            data[MAXMASS-1][i] = Wall(Color.RED)
            data[i][MAXMASS-1] = Wall(Color.RED)
            # 1じゃなくて直接配列の中にオブジェクト(壁オブジェクト)とかを入れれば、いいんじゃない？ by 06/21 22:40

        return data

    # 地形をキャンバスに描画する関数
    def draw(self):
        # for文で__dataを回して、drawしていく
        for x in range(10):
            for y in range(10):
                self.__data[x][y].create(x, y)