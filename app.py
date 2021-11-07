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
        # pyxel.init(255, 255, caption="mystery_dungeon", scale=3, fps=5)   # 5*5
        # pyxel.init(200, 200, caption="mystery_dungeon", scale=2, fps=5)     # 10*10
        pyxel.init(255, 255, caption="mystery_dungeon", scale=3, fps=10)     # 16*16
        pyxel.load("my_resource.pyxres")
        pygame.init()                                   # Pygameの初期化

        # bgm再生
        # pyxel.playm(0, loop=True)

        self.dungeon = Dungeon(_id=0)
        self.dungeon.start_turn()

        # self.floor = Floor()
        # self.camera = Camera()

        # self.floor.spawn_player()
        # self.floor.spawn_steps()


        # pygaem
        # yugothicyugothicuilight
        pyxel.run(self.update, self.draw)

    def update(self):
        self.dungeon.forward_turn()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # diplay = Display.get_instance()
        # diplay.set_screen_log()

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
        #         pygame.quit()       # Pygameの終了(画面閉じられる)

    def draw(self):
        self.dungeon.camera_show()

        pygame.display.update()     # 画面を更新

if __name__ == '__main__':
    app = App()