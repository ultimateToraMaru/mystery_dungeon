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
        self.__is_active = False
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

    @property
    def is_active(self):
        pass

    @is_active.setter
    def is_active(self, is_active):
        self.__is_active = is_active

    @is_active.getter
    def is_active(self):
        return self.__is_active

    def show(self):
        # ウィンドウ
        pyxel.rect(10, 10, 100, 100, Color.BLACK)
        pyxel.rectb(10, 10, 100, 100, Color.WHITE)

        # コンテンツを表示する
        for i, content in enumerate(self.__contents):
            str_content = str(type(self.__contents[i]).__name__)
            # カーソルインデックスのところに>を表示する
            if (self.__cursor_index == i):
                str_content = '> '+str_content

            size = 20
            pyxel.text(size, i*size+size, str_content, Color.WHITE)

        # コンテンツの表示フラグが立った時
        if (self.__contents[self.__cursor_index].is_show):
            self.__contents[self.__cursor_index].show()
            self.__is_active = False

        # アクティブな時
        if (self.__is_active):
            self.__check_move_cursor()

        self.__active_check()

    def __check_move_cursor(self):
        """
        UPキーとDOWNキーの入力をチェックしてでメニューのカーソルを操作する。
        0からメニューの数の範囲内でカーソル移動ができる
        """
        if (pyxel.btnp(pyxel.KEY_UP) and 0 < self.__cursor_index):
            self.__cursor_index -= 1
        elif (pyxel.btnp(pyxel.KEY_DOWN) and len(self.__contents)-1 > self.__cursor_index):
            self.__cursor_index += 1

        elif(pyxel.btnp(pyxel.KEY_RETURN)):
            self.__is_active = False
            self.__contents[self.__cursor_index].is_show = True
            self.__contents[self.__cursor_index].is_active = True

        elif(pyxel.btnp(pyxel.KEY_LEFT)):
            print('閉じる')
            self.__is_active = False

    def __active_check(self):
        """
        コンテンツの表示状況をみて、自分自身をアクティブにするか決める<br>
        コンテンツウィンドウがアクティブの時：False<br>
        コンテンツウィンドウが非アクティブの時：True
        """
        self.__is_active = True

        for i, content in enumerate(self.__contents):
            if (content.is_active == True):
                self.__is_active = False
                return
