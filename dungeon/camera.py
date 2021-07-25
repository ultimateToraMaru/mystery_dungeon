# 描画する部分を格納する配列を持つカメラ
from dungeon.room.object_layers.objects.none_obj import None_obj


class Camera():
    def __init__(self):
        self.__CAMERA_SCALE = 5
        self.__angle_of_view = [[None_obj()] * self.__CAMERA_SCALE for i in range(self.__CAMERA_SCALE)] 
        for i in range(self.__CAMERA_SCALE):
            for j in range(self.__CAMERA_SCALE):
                self.__angle_of_view[i][j] = None_obj()
    
    # cameraに表示したいレイヤーをセットしていく(プレイヤーを中心として上下左右5マス程度？)
    def set_camera(self):
        pass
    
    # 複数のレイヤーを合成して、一つの配列を作成する
    def create_view(self):
        pass