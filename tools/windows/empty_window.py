from dungeon.const.color import Color
from dungeon.room.object_layers.objects.player import Player
from dungeon.const.size import Size
from dungeon.room.room import Room
from dungeon.room.object_layers.objects.none_obj import None_obj
import time
import pyxel

class Empty_window():
    def __init__(self, contents=[]):
        self.__is_show = False
        self.__cursor_index = 0
        self.__contents: list = contents

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
    def cursor_index(self):
        pass

    @cursor_index.setter
    def cursor_index(self, cursor_index):
        self.__cursor_index = cursor_index

    @cursor_index.getter
    def cursor_index(self):
        return self.__cursor_index

    @property
    def contents(self):
        pass

    @contents.setter
    def contents(self, contents):
        self.__contents = contents

    @contents.getter
    def contents(self):
        return self.__contents

    def show(self):
        # 真っ黒で上書きする
        pyxel.rect(0, 0, 1000, 1000, Color.BLACK)

        for i, m in enumerate(self.__contents):
            str_menu = str(type(self.__contents[i]).__name__)
            if (self.__cursor_index == i):
                str_menu += ' <'

            size = 10
            pyxel.text(size, i*size+size, str_menu, Color.WHITE)

        if (self.__contents[self.__cursor_index].is_show):
            self.__contents[self.__cursor_index].show()

    def check_move_cursor(self):
        """
        UPキーとDOWNキーの入力をチェックしてでメニューのカーソルを操作する。
        0からメニューの数の範囲内でカーソル移動ができる
        """
        if (pyxel.btnp(pyxel.KEY_UP) and 0 < self.__cursor_index):
            self.__cursor_index -= 1
        elif (pyxel.btnp(pyxel.KEY_DOWN) and len(self.__contents)-1 > self.__cursor_index):
            self.__cursor_index += 1

        elif(pyxel.btnp(pyxel.KEY_RETURN)):
            self.__contents[self.__cursor_index].is_show = not self.__contents[self.__cursor_index].is_show