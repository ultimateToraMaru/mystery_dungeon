from dungeon.const.color import Color
from tools.windows.empty_window import Empty_window
from tools.windows.pocket_window import Pocket_window
from dungeon.room.object_layers.objects.orange import Orange
import pyxel


class Menu_window(Empty_window):
    def __init__(self):
        super().__init__([Pocket_window()])
        # self.__is_show = False
        # self.__cursor_index = 0
        # self.__contents = [Pocket_window()]
        # super().contents = [Pocket_window()]

    def set_pocket_contents(self, pocket_contents):
        """
        ポケットメニューにポケットの中身をセットする
        """
        super().contents[0].contents = pocket_contents

    # @property
    # def is_show(self):
    #     pass

    # @is_show.setter
    # def is_show(self, is_show):
    #     self.__is_show = is_show

    # @is_show.getter
    # def is_show(self):
    #     return self.__is_show

    # def show(self):
    #     # 真っ黒で上書きする
    #     pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

    #     for i, m in enumerate(self.__contents):
    #         str_menu = str(type(self.__contents[i]).__name__)
    #         if (self.__cursor_index == i):
    #             str_menu += ' <'

    #         size = 10
    #         pyxel.text(size, i*size+size, str_menu, Color.WHITE)

    #     if (self.__contents[self.__cursor_index].is_show):
    #         self.__contents[self.__cursor_index].show()

    # def check_move_cursor(self):
    #     """
    #     UPキーとDOWNキーの入力をチェックしてでメニューのカーソルを操作する。
    #     0からメニューの数の範囲内でカーソル移動ができる
    #     """
    #     if (pyxel.btnp(pyxel.KEY_UP) and 0 < self.__cursor_index):
    #         self.__cursor_index -= 1
    #     elif (pyxel.btnp(pyxel.KEY_DOWN) and len(self.__contents)-1 > self.__cursor_index):
    #         self.__cursor_index += 1

    #     elif(pyxel.btnp(pyxel.KEY_RETURN)):
    #         self.__contents[self.__cursor_index].is_show = not self.__contents[self.__cursor_index].is_show

    # def __show_pocket(self):
    #     # 真っ黒で上書きする
    #     pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

    #     for item in self.__pocket_contents:
    #         pyxel.text(str(item))