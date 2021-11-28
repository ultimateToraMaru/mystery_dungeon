import time
from dungeon.room.object_layers.empty_layer import Empty_layer
from dungeon.room.object_layers.objects.none_obj import None_obj
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__dataにWallやTile, Rockが入る
class Terrain_layer(Empty_layer):
    def __init__(self, is_room, path_way_type):
        super().__init__()
        # 地形データ(木や壁)や落ちてるアイテム(アイテムは取得したら床オブジェクトを設置)を表す変数
        # そうすればterrain_dataとterrainを分ける必要はない！
        self.data = [[Wall(Color.BROWN)] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]

        self.data = self.setExportPoints(self.data, Size.MAX_MASS_IN_ROOM_ONE_SIDE, path_way_type)
        if (is_room == True):
            self.data = self.generate(self.data, Size.MAX_MASS_IN_ROOM_ONE_SIDE)

        # elif (is_room == False):
            # self.data = self.generate_none_room(self.data)

    # 地形をランダムで形成する関数
    def generate(self, data, MAXMASS):

        # 部屋の端っこ。始まりポイントと終わりポイント
        start_point = 1
        margin = MAXMASS - (MAXMASS/2)
        end_point = MAXMASS - 1

        # 四角形の4点をランダムで決める
        r_start_x = random.randint(start_point, start_point+3)
        r_end_x = random.randint(r_start_x+margin, end_point)
        r_start_y = random.randint(start_point, start_point+3)
        r_end_y = random.randint(r_start_y+margin, end_point)

        # Y軸の端っこに床を配置していく
        for r_x in range(r_start_y, r_end_y):
            for r_y in range(r_start_x, r_end_x):
                # print(i, j)
                data[r_x][r_y] = Tile()

        # X軸の端っこに床を配置していく
        for r_x in range(r_start_x, r_end_x):
            for r_y in range(r_start_y, r_end_y):
                data[r_y][r_x] = Tile()

        return data

    # 壁だけの部屋を生成。部屋ではない。。。
    # 格子状に道を作って道の生成を簡易的にしよう
    # 階の周りを大きく壁で加工必要がある。ん？でも床ではないから歩けないか。。。囲わなくても大丈夫そう。
    def generate_none_room(self, data):
        # data = [[Wall(Color.BROWN)] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]

        for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            data[i][math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)] = Tile()
            data[math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)][i] = Tile()

        return data

    # # 地形をキャンバスに描画する関数
    # def draw(self, p_x, p_y, size):
    #     for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
    #         for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
    #             super().data[r_x][r_y].create(r_x+p_x, r_y+p_y, size)

    # 入り口出口は部屋が持つべきだよね。ってことで、地形データ(terrain_layer)に持ってきたのだ
    # 部屋間の道はその道が通る部屋が持つべきだよね。
    def setExportPoints(self, data, MAXMASS, path_way_type):

        for i in range(random.randint(1, 4)):
            # 出口ポイントをランダムで決めて、道をつくる
            center = math.floor(MAXMASS/2)
            # directions_r = random.randint(0, 3)
            for i in range(center):
                if (path_way_type == 'normal'):
                    data[0+i][center] = Tile()      # 左方
                    data[center+i][center] = Tile() # 右方
                    data[center][0+i] = Tile()      # 上方
                    data[center][center+i] = Tile() # 下方

                elif(path_way_type == 'top_end'):
                    data[0+i][center] = Tile()      # 左方
                    data[center+i][center] = Tile() # 右方
                    data[center][center+i] = Tile() # 下方

                elif(path_way_type == 'bottom_end'):
                    data[0+i][center] = Tile()      # 左方
                    data[center+i][center] = Tile() # 右方
                    data[center][0+i] = Tile()      # 上方

                elif(path_way_type == 'top_left_corner'):
                    data[center+i][center] = Tile() # 右方
                    data[center][center+i] = Tile() # 下方

                elif(path_way_type == 'bottom_left_corner'):
                    data[center+i][center] = Tile() # 右方
                    data[center][0+i] = Tile()      # 上方

                elif(path_way_type == 'left_end'):
                    data[center+i][center] = Tile() # 右方
                    data[center][0+i] = Tile()      # 上方
                    data[center][center+i] = Tile() # 下方

                elif(path_way_type == 'top_right_corner'):
                    data[0+i][center] = Tile()      # 左方
                    data[center][center+i] = Tile() # 下方

                elif(path_way_type == 'bottom_right_corner'):
                    data[0+i][center] = Tile()      # 左方
                    data[center][0+i] = Tile()      # 上方

                elif(path_way_type == 'right_end'):
                    data[0+i][center] = Tile()      # 左方
                    data[center][0+i] = Tile()      # 上方
                    data[center][center+i] = Tile() # 下方



        # path_finding()

        return data

    # # pass_findingはfloor()でやるべきなのでは？
    # def path_finding():
    #     pass

    # def set_point(self):
    #     super().data[math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)][math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)] = Wall(Color.GREEN)
