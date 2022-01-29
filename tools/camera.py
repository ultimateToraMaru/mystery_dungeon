# 描画する部分を格納する配列を持つカメラ
from tools.windows.menu_window import Menu_window
from tools.windows.map_window import Map_window
from tools.windows.eye_catching import Eye_catching
from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj
import time
import pyxel


class Camera():
    """
    ゲーム画面を写すクラス\n
    - メニューやマップのウィンドウの制御も担う
    """
    def __init__(self):
        self.__CAMERA_SCALE = 5
        self.__target = [[None_obj()] * self.__CAMERA_SCALE for i in range(self.__CAMERA_SCALE)]
        # self.__floor_rooms_data = []
        for i in range(self.__CAMERA_SCALE):
            for j in range(self.__CAMERA_SCALE):
                self.__target[i][j] = None_obj()

        # ウィンドウたち(キー入力で任意のウィンドウを表示する)
        self.__menu_window = Menu_window()
        self.__map_window = Map_window()
        self.__eye_catching = Eye_catching()

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

    def set_pocket_contents(self, pocket_contents):
        self.__menu_window.set_pocket_contents(pocket_contents)

    def stand_by(self):

        # マップウィンドウが活性の時
        if (self.__map_window.is_show):
            self.__map_window.show()

        # メニューウィンドウが活性の時
        elif(self.__menu_window.is_show):
            result = self.__menu_window.show()

            if (result != None):
                self.__menu_window.is_show = False

            return result
            # self.__menu_window.check_move_cursor()

        # それ以外の時は通常のゲーム画面を写す
        else:
            self.__show_room()
            self.__map_window.add_map(self.__target)
            self.__embed_room_address()
            self.__embed_player_hp()

        # キーボード入力を受け付ける
        if (pyxel.btnp(pyxel.KEY_F)):
            self.__map_window.is_show = not self.__map_window.is_show

            # 真っ黒で上書きする
            pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        if (pyxel.btnp(pyxel.KEY_X)):
            self.__menu_window.is_show = not self.__menu_window.is_show

            # 真っ黒で上書きする
            # pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        if (self.__eye_catching.is_show()):
            self.__eye_catching.show()

    def __embed_room_address(self):
        """
        ルームアドレスを下側に埋め込むメソッド
        """
        # ウィンドウ
        pyxel.rect(160, 25, 40, 30, Color.BLACK)
        pyxel.rectb(160, 25, 40, 30, Color.WHITE)

        # ルームアドレス
        str_room_address = '('+', '.join(map(str, self.__target.room_address))+')'
        pyxel.text(x=162, y=35, s='Room', col=Color.WHITE)
        pyxel.text(x=162, y=45, s=str_room_address, col=Color.WHITE)

    def __embed_player_hp(self):
        """
        プレイヤーのHPを下側に埋め込むメソッド
        """
        player_position = self.__target.layers.player_layer.get_player_position()

        # プレイヤーがワープトラップに引っかかった時は、ワープ直後のプレイヤーをうまく取得できないので
        # IndexErrorが発生してしまう。これは、一時的なものなので例外をキャッチして何もしない
        try :
            player = self.__target.layers.player_layer.data[player_position[0]][player_position[1]]

            # ウィンドウ
            pyxel.rect(160, 5, 40, 25, Color.BLACK)
            pyxel.rectb(160, 5, 40, 25, Color.WHITE)

            # HP描画
            str_player_hp = str(player.hp)+'/'+str(player.max_hp)
            pyxel.text(x=162, y=10, s='HP', col=Color.WHITE)
            pyxel.text(x=162, y=20, s=str_player_hp, col=Color.WHITE)

        except IndexError as e :
            # 何もしない。
            pass

    def __show_room(self):
        """
        プレイヤーのいる部屋を画面上に映し出すメソッド
        """
        x = 0
        y = 0

        if (Size.MASS_HEIGHT == 5 and Size.MASS_WIDTH == 5):
            for j in range(len(self.__target)):
                for k in range(len(self.__target)):
                    x = j*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                    y = k*Size.MAX_MASS_IN_ROOM_ONE_SIDE
                    self.__target[j][k].layers.terrain_layer.draw(x, y, size=Size.MASS_HEIGHT)
                    self.__target[j][k].layers.player_layer.draw(x, y, size=Size.MASS_HEIGHT)
                    self.__target[j][k].layers.steps_layer.draw(x, y, size=Size.MASS_HEIGHT)
                    self.__target[j][k].layers.effect_layer.draw(x, y)

                    for j in range(len(self.__target[j][k].layers.enemy_layers)):
                        self.__target[j][k].layers.enemy_layers[j].draw(x, y)

        elif (Size.MASS_HEIGHT == 16 and Size.MASS_WIDTH == 16):

            self.__target.layers.terrain_layer.draw(x, y, size=Size.MASS_HEIGHT)
            self.__target.layers.steps_layer.draw(x, y, size=Size.MASS_HEIGHT)
            self.__target.layers.trap_layer.draw(x, y, size=Size.MASS_HEIGHT)
            self.__target.layers.item_layer.draw(x, y, size=Size.MASS_HEIGHT)
            self.__target.layers.player_layer.draw(x, y, size=Size.MASS_HEIGHT)

            for i in range(len(self.__target.layers.enemy_layers)):
                self.__target.layers.enemy_layers[i].draw(x, y)

            self.__target.layers.effect_layer.draw(x, y)

    def start_eye_catching(self, dungeon_name, floor_index):
        """
        アイキャッチ(hoge dungeon 00F)を開始するメソッド
        """
        self.__eye_catching.set_index(dungeon_name, floor_index)
    #     self.__eye_catching_count = 30
    #     self.__target_floor_index = floor_index

    def clear_map(self):
        self.__map_window.clear_map(self.__target)

    def set_floor_rooms_data(self, floor_rooms_data):
        self.__map_window.floor_rooms_data = floor_rooms_data

    def show_game_clear(self):
        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        # テキストをセット
        pyxel.text(x=Size.MASS_HEIGHT*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE/2, y=Size.MASS_WIDTH*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-Size.MASS_WIDTH, s='GAME CLEAR', col=Color.WHITE)

    def show_game_over(self):
        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        # テキストをセット
        pyxel.text(x=Size.MASS_HEIGHT*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE/2, y=Size.MASS_WIDTH*Size.MAX_BLOCKS_IN_FLOOR_ONE_SIDE-Size.MASS_WIDTH, s='GAME OVER', col=Color.WHITE)