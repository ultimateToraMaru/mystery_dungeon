import math
from dungeon.const.properties import Properties
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Terrain_layer():
    def __init__(self, type):
        # 地形データ(木や壁)や落ちてるアイテム(アイテムは取得したら床オブジェクトを設置)を表す変数
        # そうすればterrain_dataとterrainを分ける必要はない！
        if (type == 'normal'):
            self.__data = [[Wall(Color.RED)] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)]      
            self.__data = self.generate(self.__data, Properties.MAX_MASS_IN_ROOM_ONE_SIDE)
        elif(type == 'none'):
            self.__data = [[Wall(Color.BROWN)] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)]
            self.__data = self.generate_none_room(self.__data)


    # 地形をランダムで形成する関数
    def generate(self, data, MAXMASS):
        # まずは四方に壁を作る
        # for i in range(MAXMASS):
        #     data[0][i] = Wall(Color.RED)
        #     data[i][0] = Wall(Color.RED)
        #     data[MAXMASS-1][i] = Wall(Color.RED)
        #     data[i][MAXMASS-1] = Wall(Color.RED)

        # 部屋の端っこ。始まりポイントと終わりポイント
        start_point = 2
        end_point = MAXMASS-1
        
        # 四角形の4点をランダムで決める
        r_x_start = random.randint(start_point, start_point+2) 
        r_x_end = random.randint(r_x_start+start_point, end_point) 
        r_y_start = random.randint(start_point, start_point+2) 
        r_y_end = random.randint(r_y_start+start_point, end_point) 

        # Y軸の端っこに床を配置していく
        for i in range(r_y_start, r_y_end):
            for j in range(r_x_start, r_x_end):
                data[i][j] = Tile(Color.GREEN)

        # X軸の端っこに床を配置していく
        for i in range(r_x_start, r_x_end):
            for j in range(r_y_start, r_y_end):
                data[j][i] = Tile(Color.GREEN)
            
        return data

    # 壁だけの部屋を生成。部屋ではない。。。
    # 格子状に道を作って道の生成を簡易的にしよう
    # 階の周りを大きく壁で加工必要がある。ん？でも床ではないから歩けないか。。。囲わなくても大丈夫そう。
    def generate_none_room(self, data):
        data = [[Wall(Color.BROWN)] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)]
        
        for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
            data[i][math.floor(Properties.MAX_MASS_IN_ROOM_ONE_SIDE/2)] = Tile(Color.GREEN)
            data[math.floor(Properties.MAX_MASS_IN_ROOM_ONE_SIDE/2)][i] = Tile(Color.GREEN)
    

        return data

    # 地形をキャンバスに描画する関数
    def draw(self, room_x, room_y):
        # for文で__dataを回して、drawしていく
        for x in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
            for y in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE):
                self.__data[x][y].create(x+room_x, y+room_y)
    