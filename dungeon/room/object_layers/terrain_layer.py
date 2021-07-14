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
            self.__data = self.setExportPoints(self.__data, Properties.MAX_MASS_IN_ROOM_ONE_SIDE-1);
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
        r_start_x = random.randint(start_point, start_point+2) 
        r_end_x = random.randint(r_start_x+start_point, end_point) 
        r_start_y = random.randint(start_point, start_point+2) 
        r_end_y = random.randint(r_start_y+start_point, end_point) 

        # 出口ポイントをランダムで決める
        r_exit_point_x_1 = random.randint(r_start_x+1, r_end_x-1)
        r_exit_point_x_2 = random.randint(r_start_x+1, r_end_x-1)
        r_exit_point_y_3 = random.randint(r_start_y+1, r_end_y-1)
        r_exit_point_y_4 = random.randint(r_start_y+1, r_end_y-1)

        print(r_exit_point_x_1, r_exit_point_x_2, r_exit_point_y_3, r_exit_point_y_4)

        # r = random.randint(1, 3)
        # point_r = random.randint(0, MAXMASS-1)

    # if (side_r == 0):
        data[r_start_y-1][r_exit_point_x_1] = Tile(Color.GREEN)
    # elif (side_r == 1):
        data[r_end_y][r_exit_point_x_2] = Tile(Color.GREEN)
    # elif (side_r == 2):
        data[r_exit_point_y_3][r_start_x-1] = Tile(Color.GREEN)
    # elif (side_r == 3):
        data[r_exit_point_y_4][r_end_x] = Tile(Color.GREEN)

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
        # r = random.randint(1, 3)
        # for i in range(r):
        #     side_r = random.randint(0, MAXMASS-1)
        #     point_r = random.randint(0, MAXMASS-1)

        #     if (side_r == 0):
        #         data[1][point_r] = Tile(Color.GREEN)
        #     elif (side_r == 1):
        #         data[MAXMASS-1][point_r] = Tile(Color.GREEN)
        #     elif (side_r == 2):
        #         data[point_r][1] = Tile(Color.GREEN)
        #     elif (side_r == 3):
        #         data[point_r][MAXMASS-1] = Tile(Color.GREEN)
        data
        
        return data


            

        # 部屋じゃないブロックは格子状に床を配置して
        # 簡易的に道を作っていくのもいいかも
        # 試しにやってみたぞい by0713
    