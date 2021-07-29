# 描画する部分を格納する配列を持つカメラ
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj


class Camera():
    def __init__(self):
        self.__CAMERA_SCALE = 5
        # self.__angle_of_view = [[None_obj()] * self.__CAMERA_SCALE for i in range(self.__CAMERA_SCALE)] 
        # for i in range(self.__CAMERA_SCALE):
        #     for j in range(self.__CAMERA_SCALE):
        #         self.__angle_of_view[i][j] = None_obj()
        self.__target_room = Room('normal', False)
        self.__player_position = [0, 0]
    
    @property
    def target_room(self):
        pass

    @target_room.setter
    def target_room(self, target_room):
        self.__target_room = target_room
    
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
        # for i in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
        #     for j in range(Size.MAX_MASS_IN_ROOM_ONE_SIDE):
        #         x = i*Size.MAX_MASS_IN_ROOM_ONE_SIDE
        #         y = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE
        #         # print(self.__target_room)
        # print(self.__player_position.index(Player()))
        self.__target_room.layers.terrain_layer.draw(x, y)
        self.__target_room.layers.player_layer.draw(x, y)