from dungeon.display import Display
from dungeon.dungeon import Dungeon
from dungeon.camera import Camera
from dungeon.room.object_layers.objects.player import Player
from dungeon.room.object_layers.objects.none_obj import None_obj
from dungeon.floor import Floor
import pyxel
import pygame
from dungeon.room.room import Room


class App:
    def __init__(self):
        # pyxel初期化処理
        # pyxel.init(255, 255, caption="mystery_dungeon", scale=3, fps=5)   # 5*5
        # pyxel.init(200, 200, caption="mystery_dungeon", scale=2, fps=5)     # 10*10
        pyxel.init(255, 255, caption="mystery_dungeon", scale=3, fps=10)     # 16*16
        pyxel.load("my_resource.pyxres")

        # pygame初期化処理
        pygame.init()

        # bgm再生
        # pyxel.playm(0, loop=True)

        # ダンジョンを生成してゲームを始める
        self.dungeon = Dungeon(_id=0)
        self.dungeon.start_turn()

        pyxel.run(self.update, self.draw)

    # ゲーム処理の更新
    def update(self):
        self.dungeon.forward_turn()

        # Qキーでゲームを終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    # 描画処理の更新
    def draw(self):
        # ゲーム画面を更新
        self.dungeon.camera_show()

        # ダンジョンログ画面を更新
        pygame.display.update()

if __name__ == '__main__':
    app = App()