from dungeon.const.color import Color
from tools.pocket_window import Pocket_window
from dungeon.room.object_layers.objects.orange import Orange
import pyxel


class Menu_window():
    def __init__(self):
        self.__is_show = False
        # self.__pocket_contents = []
        self.__cursor_index = 0
        self.__menu_list = [Pocket_window()]

    def set_pocket_contents(self, pocket_contents):
        """
        ポケットメニューにポケットの中身をセットする
        """
        self.__menu_list[0].pocket_contents = pocket_contents

    @property
    def is_show(self):
        pass

    @is_show.setter
    def is_show(self, is_show):
        self.__is_show = is_show

    @is_show.getter
    def is_show(self):
        return self.__is_show

    def show(self):
        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        for i, m in enumerate(self.__menu_list):
            str_menu = str(type(self.__menu_list[i]).__name__)
            if (self.__cursor_index == i):
                str_menu += ' <'

            size = 10
            pyxel.text(size, i*size+size, str_menu, Color.WHITE)

        if (self.__menu_list[self.__cursor_index].is_show):
            self.__menu_list[self.__cursor_index].show()

    def check_move_cursor(self):
        """
        UPキーとDOWNキーの入力をチェックしてでメニューのカーソルを操作する。
        0からメニューの数の範囲内でカーソル移動ができる
        """
        if (pyxel.btnp(pyxel.KEY_UP) and 0 < self.__cursor_index):
            self.__cursor_index -= 1
        elif (pyxel.btnp(pyxel.KEY_DOWN) and len(self.__menu_list)-1 > self.__cursor_index):
            self.__cursor_index += 1

        elif(pyxel.btnp(pyxel.KEY_RETURN)):
            self.__menu_list[self.__cursor_index].is_show = not self.__menu_list[self.__cursor_index].is_show

    # def __show_pocket(self):
    #     # 真っ黒で上書きする
    #     pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

    #     for item in self.__pocket_contents:
    #         pyxel.text(str(item))