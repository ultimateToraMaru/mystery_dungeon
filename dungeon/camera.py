# 描画する部分を格納する配列を持つカメラ
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj


class Camera():
    def __init__(self):
        self.__CAMERA_SCALE = 5
        self.__target = [[None_obj()] * self.__CAMERA_SCALE for i in range(self.__CAMERA_SCALE)] 
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
            for i in range(len(self.__target)):
                for j in range(len(self.__target)):
                    x = i*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                    y = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                    self.__target[i][j].layers.terrain_layer.draw(x, y)
                    self.__target[i][j].layers.player_layer.draw(x, y)
                    self.__target[i][j].layers.player_layer.draw(x, y)
                    self.__target[i][j].layers.enemy_layer.draw(x, y)

        # 16*16
        elif (Size.MASS_HEIGHT == 16 and Size.MASS_WIDTH == 16):
            self.__target.layers.terrain_layer.draw(x, y)
            self.__target.layers.steps_layer.draw(x, y)
            self.__target.layers.player_layer.draw(x, y)
            self.__target.layers.enemy_layer.draw(x, y)
        