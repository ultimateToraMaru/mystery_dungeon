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

        # bgm再生
        pyxel.playm(0, loop=True)

        self.dungeon = Dungeon(_id=0)
        self.dungeon.start_turn()

        # self.floor = Floor()
        # self.camera = Camera()

        # self.floor.spawn_player()
        # self.floor.spawn_steps()

        pyxel.run(self.update, self.draw)

        # pygaem
        pygame.init()                                   # Pygameの初期化
        pygame.display.set_caption("Test")              # タイトルバーに表示する文字

    def update(self):
        self.dungeon.forward_turn()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
        #         pygame.quit()       # Pygameの終了(画面閉じられる)

    def draw(self):
        self.dungeon.camera_show()

        screen = pygame.display.set_mode((400, 300))    # 大きさ400*300の画面を生成
        screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし
        pygame.display.update()     # 画面を更新
        # イベント処理
        # self.camera.target = self.floor.get_player_room_arounds()
        # self.camera.show()
    #     self.floor.terrain_draw()
    #     self.input_check()
    #     self.floor.player_set_position()
    #     self.floor.player_draw()

    # def input_check(self):
    #     if pyxel.btnp(pyxel.KEY_D):
    #         self.__now_floor.player_move('right')
    #     elif pyxel.btnp(pyxel.KEY_A):
    #         self.__now_floor.player_move('left')
    #     elif pyxel.btnp(pyxel.KEY_W):
    #         self.__now_floor.player_move('up')
    #     elif pyxel.btnp(pyxel.KEY_S):
    #         self.__now_floor.player_move('down')

if __name__ == '__main__':
    app = App()