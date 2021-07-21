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
            self.__data = [[Wall(Color.MAGENTA)] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)]      
            self.__data = self.generate(self.__data, Properties.MAX_MASS_IN_ROOM_ONE_SIDE)
            self.__data = self.setExportPoints(self.__data, Properties.MAX_MASS_IN_ROOM_ONE_SIDE)
            
        elif(type == 'none'):
            self.__data = [[Wall(Color.BROWN)] * Properties.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Properties.MAX_MASS_IN_ROOM_ONE_SIDE)]
            self.__data = self.generate_none_room(self.__data)


    # 地形をランダムで形成する関数
    def generate(self, data, MAXMASS):

        # 部屋の端っこ。始まりポイントと終わりポイント
        start_point = 2
        margin = 3
        end_point = MAXMASS-1
        
        # 四角形の4点をランダムで決める
        r_start_x = random.randint(start_point, start_point+1) 
        r_end_x = random.randint(r_start_x+margin, end_point) 
        r_start_y = random.randint(start_point, start_point+1) 
        r_end_y = random.randint(r_start_y+margin, end_point) 

        # Y軸の端っこに床を配置していく
        for i in range(r_start_y, r_end_y):
            for j in range(r_start_x, r_end_x):
                data[i][j] = Tile(Color.GREEN)

        # X軸の端っこに床を配置していく
        for i in range(r_start_x, r_end_x):
            for j in range(r_start_y, r_end_y):
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

    # 入り口出口は部屋が持つべきだよね。ってことで、地形データ(terrain_layer)に持ってきたのだ
    # 部屋間の道はその道が通る部屋が持つべきだよね。
    def setExportPoints(self, data, MAXMASS):

        for i in range(random.randint(1, 4)):
            # 出口ポイントをランダムで決めて、道をつくる
            center = math.floor(MAXMASS/2)
            # directions_r = random.randint(0, 3)
            for i in range(5):
                # if (directions_r == 0):
                    data[0+i][center] = Tile(Color.GREEN)
                # elif (directions_r == 1):
                    data[center+i][center] = Tile(Color.GREEN)
                # elif (directions_r == 2):
                    data[center][0+i] = Tile(Color.GREEN)
                # elif (directions_r == 3):
                    data[center][center+i] = Tile(Color.GREEN)
        
        # path_finding()
        
        return data
    
    # pass_findingはfloor()でやるべきなのでは？
    def path_finding():
        pass

    def set_point(self):
        self.__data[math.floor(Properties.MAX_MASS_IN_ROOM_ONE_SIDE/2)][math.floor(Properties.MAX_MASS_IN_ROOM_ONE_SIDE/2)] = Wall(Color.GREEN)
    