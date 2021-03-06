import time
from dungeon.room.object_layers.empty_layer import Empty_layer
from dungeon.room.object_layers.objects.none_obj import None_obj
import math
from dungeon.const.size import Size
import random
from dungeon.room.object_layers.objects.tile import Tile
from dungeon.room.object_layers.objects.tile_path import Tile_path
from dungeon.room.object_layers.objects.tile_room import Tile_room
from dungeon.room.object_layers.objects.wall import Wall
from dungeon.const.color import Color

# 地形を表すクラス。地形データ__self.dataにWallやTile, Rockが入る
class Terrain_layer(Empty_layer):
    def __init__(self, is_room, path_way_type):
        super().__init__()
        # 地形データ(木や壁)や落ちてるアイテム(アイテムは取得したら床オブジェクトを設置)を表す変数
        # そうすればterrain_self.dataとterrainを分ける必要はない！
        self.data = [[Wall(Color.BROWN)] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]

        self.generate_path_way(path_way_type)
        if (is_room == True):
            self.generate_room()

        # elif (is_room == False):
            # self.self.data = self.generate_none_room(self.self.data)

    # 地形をランダムで形成する関数
    def generate_room(self):
        MAXMASS = Size.MAX_MASS_IN_ROOM_ONE_SIDE

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
                self.data[r_x][r_y] = Tile_room()

        # X軸の端っこに床を配置していく
        for r_x in range(r_start_x, r_end_x):
            for r_y in range(r_start_y, r_end_y):
                self.data[r_y][r_x] = Tile_room()

    # 壁だけの部屋を生成。部屋ではない。。。
    # 格子状に道を作って道の生成を簡易的にしよう
    # 階の周りを大きく壁で加工必要がある。ん？でも床ではないから歩けないか。。。囲わなくても大丈夫そう。
    def generate_none_room(self):
        # self.data = [[Wall(Color.BROWN)] * Size.MAX_MASS_IN_ROOM_ONE_SIDE for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE)]

        for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
            self.data[i][math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)] = Tile_path()
            self.data[math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)][i] = Tile_path()

        return self.data

    # # 地形をキャンバスに描画する関数
    # def draw(self, p_x, p_y, size):
    #     for r_x in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
    #         for r_y in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
    #             super().self.data[r_x][r_y].create(r_x+p_x, r_y+p_y, size)

    # 入り口出口は部屋が持つべきだよね。ってことで、地形データ(terrain_layer)に持ってきたのだ
    # 部屋間の道はその道が通る部屋が持つべきだよね。
    def generate_path_way(self, path_way_type):
        MAXMASS = Size.MAX_MASS_IN_ROOM_ONE_SIDE

        for i in range(random.randint(1, 4)):
            # 出口ポイントをランダムで決めて、道をつくる
            center = math.floor(MAXMASS/2)
            # directions_r = random.randint(0, 3)
            for i in range(center):
                if (path_way_type == 'normal'):
                    self.data[0+i][center] = Tile_path()      # 左方
                    self.data[center+i][center] = Tile_path() # 右方
                    self.data[center][0+i] = Tile_path()      # 上方
                    self.data[center][center+i] = Tile_path() # 下方

                elif(path_way_type == 'top_end'):
                    self.data[0+i][center] = Tile_path()      # 左方
                    self.data[center+i][center] = Tile_path() # 右方
                    self.data[center][center+i] = Tile_path() # 下方

                elif(path_way_type == 'bottom_end'):
                    self.data[0+i][center] = Tile_path()      # 左方
                    self.data[center+i][center] = Tile_path() # 右方
                    self.data[center][0+i] = Tile_path()      # 上方

                elif(path_way_type == 'top_left_corner'):
                    self.data[center+i][center] = Tile_path() # 右方
                    self.data[center][center+i] = Tile_path() # 下方

                elif(path_way_type == 'bottom_left_corner'):
                    self.data[center+i][center] = Tile_path() # 右方
                    self.data[center][0+i] = Tile_path()      # 上方

                elif(path_way_type == 'left_end'):
                    self.data[center+i][center] = Tile_path() # 右方
                    self.data[center][0+i] = Tile_path()      # 上方
                    self.data[center][center+i] = Tile_path() # 下方

                elif(path_way_type == 'top_right_corner'):
                    self.data[0+i][center] = Tile_path()      # 左方
                    self.data[center][center+i] = Tile_path() # 下方

                elif(path_way_type == 'bottom_right_corner'):
                    self.data[0+i][center] = Tile_path()      # 左方
                    self.data[center][0+i] = Tile_path()      # 上方

                    self.data[center][center] = Tile_path()   # 中央(調整)

                elif(path_way_type == 'right_end'):
                    self.data[0+i][center] = Tile_path()      # 左方
                    self.data[center][0+i] = Tile_path()      # 上方
                    self.data[center][center+i] = Tile_path() # 下方


    # # pass_findingはfloor()でやるべきなのでは？
    # def path_finding():
    #     pass

    # def set_point(self):
    #     super().self.data[math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)][math.floor(Size.MAX_MASS_IN_ROOM_ONE_SIDE/2)] = Wall(Color.GREEN)
