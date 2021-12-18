from dungeon.const.color import Color
import pyxel

class Pocket_window():
    def __init__(self):
        self.__is_show = False
        self.__cursor_index = 0
        self.__pocket_contents: list = []

    @property
    def is_show(self):
        pass

    @is_show.setter
    def is_show(self, is_show):
        self.__is_show = is_show

    @is_show.getter
    def is_show(self):
        return self.__is_show

    @property
    def pocket_contents(self):
        pass

    @pocket_contents.setter
    def pocket_contents(self, pocket_contents):
        self.__pocket_contents = pocket_contents

    def __show_pocket(self):
        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        for item in self.__pocket_contents:
            pyxel.text(str(item))

    def show(self):
        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        for i, item in enumerate(self.__pocket_contents):
            str_menu = str(type(item).__name__)
            if (self.__cursor_index == i):
                str_menu += ' <'

            size = 10
            pyxel.text(size, i*size+size, str_menu, Color.WHITE)

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
            self.__menu_list[self.__cursor_index].show()