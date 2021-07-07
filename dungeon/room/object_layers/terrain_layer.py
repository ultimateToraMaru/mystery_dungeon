from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Terrain_layer():
    def __init__(self, type):
        self.__MAXMASS = 10     # 部屋の一辺の最大マス数を表す変数
        # 地形データ(木や壁)や落ちてるアイテム(アイテムは取得したら床オブジェクトを設置)を表す変数
        # そうすればterrain_dataとterrainを分ける必要はない！
        if (type == 'normal'):
            self.__data = [[Tile(Color.BLACK)] * self.__MAXMASS for i in range(self.__MAXMASS)]      
            self.__data = self.generate(self.__data, self.__MAXMASS)
        elif(type == 'none'):
            self.__data = [[Wall(Color.BLACK)] * self.__MAXMASS for i in range(self.__MAXMASS)]

    # 地形をランダムで形成する関数
    def generate(self, data, MAXMASS):
        # まずは四方に壁を作る
        for i in range(MAXMASS):
            data[0][i] = Wall(Color.RED)
            data[i][0] = Wall(Color.RED)
            data[MAXMASS-1][i] = Wall(Color.RED)
            data[i][MAXMASS-1] = Wall(Color.RED)
            
        return data

    # 壁だけの部屋を生成。部屋ではない。。。
    def generate_none_room(self):
        data = [[Wall(Color.BLACK)] * self.__MAXMASS for i in range(self.__MAXMASS)]
        return data

    # 地形をキャンバスに描画する関数
    def draw(self):
        # for文で__dataを回して、drawしていく
        for x in range(10):
            for y in range(10):
                self.__data[x][y].create(x, y)
    