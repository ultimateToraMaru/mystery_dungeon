from dungeon.const.color import Color
from dungeon.room.object_layers.objects.orange import Orange
import pyxel
from tools.windows.empty_window import Empty_window

class Pocket_window(Empty_window):
    def __init__(self):
        super().__init__()

    def show(self):
        # ウィンドウ
        pyxel.rect(20, 20, 100, 100, Color.BLACK)
        pyxel.rectb(20, 20, 100, 100, Color.WHITE)

        for i, item in enumerate(super().contents):
            str_content = str(type(item).__name__)
            # print(str_content)
            if (super().cursor_index == i):
                str_content = '> ' + str_content

            size = 30
            pyxel.text(size, i*10+size, str_content, Color.WHITE)

        if (super().is_active):
            return self.__check_move_cursor()

    def __check_move_cursor(self):
        """
        UPキーとDOWNキーの入力をチェックしてでメニューのカーソルを操作する。
        0からメニューの数の範囲内でカーソル移動ができる
        """
        if (pyxel.btnp(pyxel.KEY_UP) and 0 < super().cursor_index):
            self.cursor_index -= 1
        elif (pyxel.btnp(pyxel.KEY_DOWN) and len(super().contents)-1 > super().cursor_index):
            self.cursor_index += 1

        # アイテムを使う
        elif(pyxel.btnp(pyxel.KEY_RETURN)):
            self.is_active = False
            item = super().contents[super().cursor_index]

            self.is_active = False
            self.is_show = False

            # アイテム使用時の効果音
            pyxel.play(0, 34, loop=False)

            return item

        elif(pyxel.btnp(pyxel.KEY_LEFT)):
            self.is_active = False
            self.is_show = False
