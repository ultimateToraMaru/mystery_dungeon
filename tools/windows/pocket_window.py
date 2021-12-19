from dungeon.const.color import Color
import pyxel
from tools.windows.empty_window import Empty_window

class Pocket_window(Empty_window):
    def __init__(self):
        super().__init__()
        # super().is_show = False
        # super().cursor_index = 0
        # super().contents: list = []

    # @property
    # def is_show(self):
    #     pass

    # @is_show.setter
    # def is_show(self, is_show):
    #     super().is_show = is_show

    # @is_show.getter
    # def is_show(self):
    #     return super().is_show

    # @property
    # def contents(self):
    #     pass

    # @contents.setter
    # def contents(self, contents):
    #     super().contents = contents

    # @contents.getter
    # def contents(self):
    #     return super().contents

    # def __show_pocket(self):
    #     # 真っ黒で上書きする
    #     pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

    #     for item in super().contents:
    #         pyxel.text(str(item))

    def show(self):
        # ウィンドウ
        pyxel.rect(20, 20, 100, 100, Color.BLACK)
        pyxel.rectb(20, 20, 100, 100, Color.WHITE)

        for i, item in enumerate(super().contents):
            str_menu = str(type(item).__name__)
            if (super().cursor_index == i):
                str_menu += ' <'

            size = 30
            pyxel.text(size, i*10+size, str_menu, Color.WHITE)

        self.__check_move_cursor()

    def __check_move_cursor(self):
        """
        UPキーとDOWNキーの入力をチェックしてでメニューのカーソルを操作する。
        0からメニューの数の範囲内でカーソル移動ができる
        """
        if (pyxel.btnp(pyxel.KEY_UP) and 0 < super().cursor_index):
            super().cursor_index -= 1
        elif (pyxel.btnp(pyxel.KEY_DOWN) and len(super().contents)-1 > super().cursor_index):
            # TODO: なぜかsuperはcursor_indexを持ってないって言われる
            super().cursor_index += 1

        elif(pyxel.btnp(pyxel.KEY_RETURN)):
            print('use')
            super().contents[super().cursor_index].use()

        elif(pyxel.btnp(pyxel.KEY_LEFT)):
            print('閉じる')
            self.__is_show = False