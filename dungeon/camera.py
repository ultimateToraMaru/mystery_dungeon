# 描画する部分を格納する配列を持つカメラ
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj
import time
import pyxel


class Camera():
    def __init__(self):
        self.__CAMERA_SCALE = 5
        self.__target = [[None_obj()] * self.__CAMERA_SCALE for i in range(self.__CAMERA_SCALE)]
        self.__floor_rooms_data = []
        for i in range(self.__CAMERA_SCALE):
            for j in range(self.__CAMERA_SCALE):
                self.__target[i][j] = None_obj()
        # self.__target = []
        self.__player_position = [0, 0]

    @property
    def target(self):
        pass

    @target.setter
    def target(self, target):
        self.__target = target

    @property
    def floor_rooms_data(self):
        pass

    @floor_rooms_data.setter
    def floor_rooms_data(self, floor_rooms_data):
        self.__floor_rooms_data = floor_rooms_data

    @property
    def player_position(self):
        pass

    @player_position.setter
    def player_position(self, player_position):
        self.__player_position = player_position

    # cameraに表示したいレイヤーをセットしていく(プレイヤーを中心として上下左右5マス程度？)
    def set_camera(self):
        pass

    # 複数のレイヤーを合成して、一つの配列を作成する
    def create_view(self):
        pass

    def show(self):
        x = 0
        y = 0
        # 5*5
        if (Size.MASS_HEIGHT == 5 and Size.MASS_WIDTH == 5):
            for j in range(len(self.__target)):
                for k in range(len(self.__target)):
                    x = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                    y = k*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                    self.__target[j][k].layers.terrain_layer.draw(x, y)
                    self.__target[j][k].layers.player_layer.draw(x, y)
                    self.__target[j][k].layers.effect_layer.draw(x, y)
                    # time.sleep(1)
                    for j in range(len(self.__target[j][k].layers.enemy_layers)):
                        self.__target[j][k].layers.enemy_layers[j].draw(x, y)

        # 16*16
        elif (Size.MASS_HEIGHT == 16 and Size.MASS_WIDTH == 16):
            self.__show_map()
            self.__target.layers.terrain_layer.draw(x, y, size=16)
            self.__target.layers.steps_layer.draw(x, y)
            self.__target.layers.player_layer.draw(x, y, size=16)
            self.__target.layers.effect_layer.draw(x, y)
            # time.sleep(1)
            for i in range(len(self.__target.layers.enemy_layers)):
                self.__target.layers.enemy_layers[i].draw(x, y)

            self.__embed_room_address()

    def __embed_room_address(self):
        str_room_address = '('+', '.join(map(str, self.__target.room_address))+')'
        pyxel.blt(x=0, y=Size.MASS_HEIGHT*10, img=0, u=0, v=48, w=48, h=16, colkey=0)
        pyxel.text(x=Size.MASS_HEIGHT/2, y=Size.MASS_HEIGHT*Size.MAX_MASS_IN_ROOM_ONE_SIDE+(Size.MASS_HEIGHT/2), s=str_room_address, col=Color.BLUE)

    def __show_map(self):
        # 全体マップ
        for i in range(len(self.__floor_rooms_data)):
            for j in range(len(self.__floor_rooms_data)):
                x = i*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                y = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE

                if (self.__target.room_address == [i, j]):
                    self.__floor_rooms_data[i][j].layers.terrain_layer.draw(x, y, size=5)
                    self.__floor_rooms_data[i][j].layers.player_layer.draw(x, y, size=5)
                # self.__floor_rooms_data[i][j].layers.effect_layer.draw(x, y)
                # # time.sleep(1)
                # for i in range(len(self.__floor_rooms_data[i][j].layers.enemy_layers)):
                #     self.__floor_rooms_data[i][j].layers.enemy_layers[j].draw(x, y)
